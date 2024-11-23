from django.contrib import admin
from django.contrib.admin import TabularInline

# Register your models here.
from .models import Playlist, PlaylistItem

class PlaylistItemInline(TabularInline):
    model = PlaylistItem

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]
    class Meta:
        model = Playlist

admin.site.register(Playlist, PlaylistAdmin)