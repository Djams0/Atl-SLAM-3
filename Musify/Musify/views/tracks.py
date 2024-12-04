import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Favorite, historical, PlaylistUser, playlist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Affichage de la vue avec les pistes et playlists de l'utilisateur
@login_required
def tracks_view(request, artist_id):
    url = f"https://api.deezer.com/artist/{artist_id}/top?limit=50"
    response = requests.get(url)
    tracks_data = []

    if response.status_code == 200:
        tracks = response.json().get("data", [])
        for track in tracks:
            tracks_data.append({
                "id": track.get("id"),
                "title": track.get("title"),
                "album": track.get("album", {}).get("title"),
                "artist": track.get("artist", {}).get("name"),
                "cover": track.get("album", {}).get("cover_medium"),
                "preview": track.get("preview"),
            })
    tracks_data = sorted(tracks_data, key=lambda x: x["album"].lower())

    # Récupérer les playlists de l'utilisateur
    playlists = PlaylistUser.objects.filter(user=request.user).select_related('playlist')
    
    return render(request, 'tracks.html', {"tracks": tracks_data, "playlists": playlists})


@login_required
def add_to_playlist(request, track_id):
    if request.method == 'POST':
        playlist_id = request.POST.get('playlist_id')
        new_playlist_name = request.POST.get('new_playlist_name')
        
        if new_playlist_name:
            new_playlist = playlist.objects.create(name=new_playlist_name)
            playlist_id = new_playlist.id

        playlist_selected = playlist.objects.get(id=playlist_id)
        PlaylistUser.objects.create(
            playlist=playlist_selected,
            user=request.user,
            id_song_deezer=track_id
        )
        return JsonResponse({"message": "song added to playlist"})
    return JsonResponse({"message": "error"}, status=400)


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
def add_to_historical(request, track_id):
    user = request.user
    historical.objects.create(
        user=user,
        id_song_deezer=track_id
    )
    return JsonResponse({"message": "song added to historical"})






