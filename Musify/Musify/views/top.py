import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Favorite, historical, playlist, PlaylistUser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@login_required
def top_view(request):
    url = "https://api.deezer.com/chart"
    response = requests.get(url)
    tracks_data = []

    if response.status_code == 200:
        tracks = response.json().get("tracks", {}).get("data", [])
        for track in tracks:
            tracks_data.append({
                "id": track.get("id"),
                "title": track.get("title"),
                "album": track.get("album", {}).get("title"),
                "artist": track.get("artist", {}).get("name"),
                "cover": track.get("album", {}).get("cover_medium"),
                "preview": track.get("preview"),
                "position": track.get("position"),
                "link": track.get("link")
            })
    playlists = playlist.objects.filter(user=request.user)
    return render(request, 'top.html', {"tracks": tracks_data, "playlists": playlists})



@login_required
def like_track(request, track_id):
    user = request.user
    favorite, created = Favorite.objects.get_or_create(
        user=user,
        id_detail_deezer=track_id,
        type="track"
    )
    if not created:
        favorite.delete()
        return JsonResponse({"message": "song unliked"})
    
    return JsonResponse({"message": "song liked"})



@login_required
def add_to_playlist(request, track_id):
    user = request.user 
    
    new_playlist_name = request.POST.get('new_playlist_name')
    playlist_id = request.POST.get('playlist_id')

    if new_playlist_name:
        
        new_playlist = playlist.objects.create(
            name=new_playlist_name,
            user=user 
        )
    else:
        if playlist_id:
            new_playlist = get_object_or_404(playlist, id=playlist_id, user=user)
        else:
            return JsonResponse({"message": "No playlist selected or created"}, status=400)

    existing_entry = PlaylistUser.objects.filter(
        playlist=new_playlist,
        id_song_deezer=track_id
    ).first()

    if existing_entry:
        return JsonResponse({"message": "Track already in playlist"}, status=400)
    
    PlaylistUser.objects.create(
        playlist=new_playlist, 
        id_song_deezer=track_id 
    )
    
    return JsonResponse({"message": "Track added to playlist"})



@login_required(login_url='/login/')
def add_to_historical(request, track_id):
    user = request.user
    historical.objects.create(
        user=user,
        id_song_deezer=track_id
    )
    return JsonResponse({"message": "song added to historical"})
