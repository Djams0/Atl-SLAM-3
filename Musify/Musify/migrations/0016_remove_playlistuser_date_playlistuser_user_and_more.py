# Generated by Django 5.1.3 on 2024-12-04 10:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musify', '0015_remove_playlistuser_user_playlist_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistuser',
            name='date',
        ),
        migrations.AddField(
            model_name='playlistuser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlistuser',
            name='id_song_deezer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='playlistuser',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musify.playlist'),
        ),
    ]
