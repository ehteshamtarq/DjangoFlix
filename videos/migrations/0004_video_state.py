# Generated by Django 5.1.3 on 2024-11-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_delete_videoproxy_videoallproxy_videopublishedproxy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
