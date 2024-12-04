import requests
from django.shortcuts import render

def home_view(request):
    base_url = "https://api.deezer.com/artist/"
    artists_data = []

    for artist_id in range(1, 34):
        response = requests.get(f"{base_url}{artist_id}")
        if response.status_code == 200:
            artist = response.json()
            if artist.get("id"):  # Vérifiez que l'ID existe
                artists_data.append({
                    "id": artist.get("id"),  # Ajoutez l'ID ici
                    "name": artist.get("name"),
                    "picture_xl": artist.get("picture_xl"),
                    "nb_album": artist.get("nb_album"),
                    "nb_fan": artist.get("nb_fan"),
                })

    return render(request, 'home.html', {"artists": artists_data})

