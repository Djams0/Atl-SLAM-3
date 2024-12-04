import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Favorite, PlaylistUser, historical

@login_required
def account_view(request):
    user = request.user

    # Récupérer le prénom et nom de l'utilisateur
    first_name = user.first_name
    last_name = user.last_name

    # Récupérer les favoris de l'utilisateur
    favorites_data = []
    favorites = Favorite.objects.filter(user=user)
    for favorite in favorites:
        if favorite.type == "track":
            # Utiliser l'API Deezer pour récupérer les informations de la track
            url = f"https://api.deezer.com/track/{favorite.id_detail_deezer}"
            response = requests.get(url)
            if response.status_code == 200:
                track = response.json()
                favorites_data.append({
                    "title": track.get("title"),
                    "artist": track.get("artist", {}).get("name"),
                    "album": track.get("album", {}).get("title"),
                    "cover": track.get("album", {}).get("cover_medium"),
                })

    # Récupérer les morceaux dans les playlists de l'utilisateur
    playlists_data = []
    playlists = PlaylistUser.objects.filter(user=user)
    for playlist in playlists:
        url = f"https://api.deezer.com/track/{playlist.id_song_deezer}"
        response = requests.get(url)
        if response.status_code == 200:
            track = response.json()
            playlists_data.append({
                "title": track.get("title"),
                "artist": track.get("artist", {}).get("name"),
                "album": track.get("album", {}).get("title"),
                "cover": track.get("album", {}).get("cover_medium"),
            })

    # Récupérer l'historique d'écoute de l'utilisateur
    history_data = []
    history = historical.objects.filter(user=user)
    for entry in history:
        url = f"https://api.deezer.com/track/{entry.id_song_deezer}"
        response = requests.get(url)
        if response.status_code == 200:
            track = response.json()
            history_data.append({
                "title": track.get("title"),
                "artist": track.get("artist", {}).get("name"),
                "album": track.get("album", {}).get("title"),
                "cover": track.get("album", {}).get("cover_medium"),
            })

    # Rendre la page avec les données
    return render(request, 'account.html', {
        "first_name": first_name,
        "last_name": last_name,
        "favorites": favorites_data,
        "playlists": playlists_data,
        "history": history_data
    })
