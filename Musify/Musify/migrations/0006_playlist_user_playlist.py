# Generated by Django 5.1.3 on 2024-11-13 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musify', '0005_playlist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist_user',
            name='playlist',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, to='Musify.playlist', verbose_name='musify_playlist'),
            preserve_default=False,
        ),
    ]