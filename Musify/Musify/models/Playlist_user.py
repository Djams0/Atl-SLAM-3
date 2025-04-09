from django.db import models
from django.contrib.auth.models import User
from .Playlist import playlist  

class PlaylistUser(models.Model):
    playlist = models.ForeignKey(playlist, on_delete=models.CASCADE)
    id_song_deezer = models.CharField(max_length=100)  

    def __str__(self):
        return f"{self.user.username} - {self.playlist.name}"


