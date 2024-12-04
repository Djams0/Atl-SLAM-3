import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Favorite, historical, PlaylistUser


def top_view(request):
    # URL de l'API Deezer pour obtenir le top 20 des morceaux
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
                "position": track.get("position"),  # Ajout de la position du morceau
                "link": track.get("link")
            })

    return render(request, 'top.html', {"tracks": tracks_data})


@login_required
def like_track(request, track_id):
    user = request.user
    favorite, created = Favorite.objects.get_or_create(
        user=user,
        id_detail_deezer=track_id,
        type="track"
    )
    if not created:
        favorite.delete()  # Unlike if it already exists

    return redirect('top')


@login_required(login_url='/login/')
def add_to_playlist(request, track_id):
    user = request.user
    
    playlist_user = user.playlistuser_set.first()
    if not playlist_user:
        playlist = playlist.objects.create(name=f"Playlist de {user.username}")
        playlist_user = PlaylistUser.objects.create(
            playlist=playlist,
            user=user,
            id_song_deezer=track_id
        )
    else:
        playlist = playlist_user.playlist
    
    PlaylistUser.objects.create(
        playlist=playlist,
        user=user,
        id_song_deezer=track_id
    )
    
    return redirect('top')



@login_required(login_url='/login/')
def add_to_historical(request, track_id):
    user = request.user
    historical.objects.create(
        user=user,
        id_song_deezer=track_id
    )
    return redirect('top')
