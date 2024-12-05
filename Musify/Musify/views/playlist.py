import requests
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import PlaylistUser, playlist

@login_required
def playlist_detail(request, playlist_id):
    # Récupérer la playlist spécifique
    user_playlist = get_object_or_404(playlist, id=playlist_id, user=request.user)

    # Récupérer les chansons de la playlist
    songs_data = []
    playlist_songs = PlaylistUser.objects.filter(playlist=user_playlist)
    for song in playlist_songs:
        # Utiliser l'API Deezer pour récupérer les informations de la chanson
        url = f"https://api.deezer.com/track/{song.id_song_deezer}"
        response = requests.get(url)
        if response.status_code == 200:
            track = response.json()
            songs_data.append({
                "title": track.get("title"),
                "artist": track.get("artist", {}).get("name"),
                "album": track.get("album", {}).get("title"),
                "cover": track.get("album", {}).get("cover_medium"),
                "preview": track.get("preview"),
            })

    # Rendre la page avec les données
    return render(request, 'playlist.html', {
        "playlist_name": user_playlist.name,
        "songs": songs_data
    })


