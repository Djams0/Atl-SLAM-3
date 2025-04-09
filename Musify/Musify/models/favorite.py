from django.db import models
from django.utils.translation import gettext_lazy as _

class Favorite(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=_("User"), on_delete=models.CASCADE)
    id_detail_deezer = models.BigIntegerField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)



