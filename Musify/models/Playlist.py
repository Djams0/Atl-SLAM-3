from django.db import models
from django.utils.translation import gettext_lazy as _

class playlist(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", verbose_name=_("User"), on_delete=models.CASCADE)
