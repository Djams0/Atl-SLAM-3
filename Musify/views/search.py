import requests
from django.shortcuts import render

def search_view(request):
    query = request.GET.get('q', '') 
    tracks = [] 

    if query:
        url = f'https://api.deezer.com/search?q={query}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            tracks = data['data']  

    return render(request, 'search.html', {'tracks': tracks, 'query': query})
