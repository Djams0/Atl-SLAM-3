# Generated by Django 5.1.3 on 2024-11-13 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musify', '0003_historycal_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
    ]
