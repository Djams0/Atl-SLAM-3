from django.db import models
from django.utils.translation import gettext_lazy as _

class historycal(models.Model):
    user = models.ForeignKey("Musify.users", verbose_name=_("musify_users"), on_delete=models.CASCADE)
    id_song_deezer = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)