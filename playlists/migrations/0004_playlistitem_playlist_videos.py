# Generated by Django 5.1.3 on 2024-11-23 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0003_alter_playlist_video'),
        ('videos', '0007_alter_video_video_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'ordering': ['order', '-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, related_name='playlist_item', through='playlists.PlaylistItem', to='videos.video'),
        ),
    ]