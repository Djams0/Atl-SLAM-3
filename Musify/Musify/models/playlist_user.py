from django.db import models
from django.utils.translation import gettext_lazy as _

class PlaylistUser(models.Model):
    playlist = models.ForeignKey("Musify.playlist", verbose_name=_("musify_playlist"), on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", verbose_name=_("User"), on_delete=models.CASCADE)
    id_song_deezer = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"PlaylistUser: {self.user.username} - {self.playlist.name}"

