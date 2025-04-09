import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Favorite, playlist, historical

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
                "id": track.get("id"),
                "title": track.get("title"),
                "album": track.get("album", {}).get("title"),
                "artist": track.get("artist", {}).get("name"),
                "cover": track.get("album", {}).get("cover_medium"),
                "preview": track.get("preview"),
                })
                
    # Récupérer les artist favoris de l'utilisateur
    artists_data = []
    artists = Favorite.objects.filter(user=user)
    for favorite in artists:
        if favorite.type == "artist":
            # Utiliser l'API Deezer pour récupérer les informations de la track
            url = f"https://api.deezer.com/artist/{favorite.id_detail_deezer}"
            response = requests.get(url)
            if response.status_code == 200:
                artist = response.json()
                artists_data.append({
                    "id": artist.get("id"),
                    "name": artist.get("name"),
                    "picture_xl": artist.get("picture_xl"),
                    "nb_album": artist.get("nb_album"),
                    "nb_fan": artist.get("nb_fan"),
                })

    # Récupérer les playlists de l'utilisateur (modifié pour afficher uniquement les noms)
    playlists_data = []
    playlists = playlist.objects.filter(user=user)
    for playlist_item in playlists:
        playlists_data.append({
            "id": playlist_item.id,
            "name": playlist_item.name,
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
                "id": track.get("id"),
                "title": track.get("title"),
                "album": track.get("album", {}).get("title"),
                "artist": track.get("artist", {}).get("name"),
                "cover": track.get("album", {}).get("cover_medium"),
                "preview": track.get("preview"),
            })

    # Rendre la page avec les données
    return render(request, 'account.html', {
        "first_name": first_name,
        "last_name": last_name,
        "favorites": favorites_data,
        "artists": artists_data,
        "playlists": playlists_data,
        "history": history_data
    })

