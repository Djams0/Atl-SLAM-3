from django.db import models
from django.utils.translation import gettext_lazy as _

class historical(models.Model):  # Utilise un nom de modèle au style PascalCase
    user = models.ForeignKey("auth.User", verbose_name=_("User"), on_delete=models.CASCADE)  # Utilise "auth.User" pour faire référence au modèle User par défaut de Django
    id_song_deezer = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historique de {self.user.username} - {self.id_song_deezer}"
