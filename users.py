from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

