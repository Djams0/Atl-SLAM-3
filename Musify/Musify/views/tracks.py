import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Favorite, historical, PlaylistUser, playlist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import logging

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
    playlists = PlaylistUser.objects.filter(playlist__user=request.user).select_related('playlist')
    
    return render(request, 'tracks.html', {"tracks": tracks_data, "playlists": playlists})




@login_required
def add_to_playlist(request, track_id):
    user = request.user  # Récupère l'utilisateur connecté

    # Récupérer le nom de la nouvelle playlist et l'ID de la playlist existante
    new_playlist_name = request.POST.get('new_playlist_name')
    playlist_id = request.POST.get('playlist_id')

    if new_playlist_name:
        # Créer une nouvelle playlist si l'utilisateur a fourni un nom de playlist
        new_playlist = playlist.objects.create(
            name=new_playlist_name,
            user=user  # Associer la playlist à l'utilisateur connecté
        )
    else:
        # Utiliser la playlist existante si un ID de playlist est fourni
        if playlist_id:
            new_playlist = get_object_or_404(playlist, id=playlist_id, user=user)
        else:
            # Si l'utilisateur n'a pas sélectionné une playlist existante et n'a pas créé de nouvelle,
            # on peut soit créer une playlist par défaut ou renvoyer une erreur.
            return JsonResponse({"message": "No playlist selected or created"}, status=400)

    # Vérifier si la chanson est déjà ajoutée à cette playlist
    existing_entry = PlaylistUser.objects.filter(
        playlist=new_playlist,
        id_song_deezer=track_id
    ).first()

    if existing_entry:
        return JsonResponse({"message": "Track already in playlist"}, status=400)

    # Ajouter l'entrée dans la table PlaylistUser pour associer la chanson à la playlist
    PlaylistUser.objects.create(
        playlist=new_playlist,  # Associer la playlist
        id_song_deezer=track_id  # Associer la chanson Deezer
    )
    
    return JsonResponse({"message": "Track added to playlist"})



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
