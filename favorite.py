from django.db import models
from django.utils.translation import gettext_lazy as _

class Favorite(models.Model):
    user = models.ForeignKey("Musify.users", verbose_name=_("musify_users"), on_delete=models.CASCADE)
    id_detail_deezer = models.BigIntegerField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)




