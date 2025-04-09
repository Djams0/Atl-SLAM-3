"""
URL configuration for Musify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views.signup import signup_view
from .views.login import login_view
from .views.logout import logout_view
from .views.home import  home_view, like_artist
from .views.account import account_view
from .views.playlist import playlist_detail
from .views.tracks import tracks_view, like_track, add_to_playlist, add_to_historical
from .views.top import top_view, like_track, add_to_playlist, add_to_historical
from .views.search import  search_view
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),

    path('tracks/<int:artist_id>/', tracks_view, name='tracks'),
    path('tracks/like/<int:track_id>/', like_track, name='like_track'),
    path('tracks/add_to_playlist/<int:track_id>/', add_to_playlist, name='add_to_playlist'),
    path('tracks/add_to_historical/<int:track_id>/', add_to_historical, name='add_to_historical'),
    path('artist/like/<int:artist_id>/', like_artist, name='like_artist'),

    
    path('top/', top_view, name='top'),
    path('search/', search_view, name='search' ),
    
    path('account/', account_view, name='account'),
    path('playlist/<int:playlist_id>/', playlist_detail, name='playlist_detail'),
]

