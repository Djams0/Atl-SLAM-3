# Generated by Django 5.1.3 on 2024-11-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musify', '0010_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
