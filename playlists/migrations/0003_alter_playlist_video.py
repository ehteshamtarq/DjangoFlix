# Generated by Django 5.1.3 on 2024-11-23 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_playlist_video'),
        ('videos', '0007_alter_video_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlist_featured', to='videos.video'),
        ),
    ]
