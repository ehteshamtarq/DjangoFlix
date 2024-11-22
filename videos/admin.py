from django.contrib import admin

# Register your models here.
from .models import VideoPublishedProxy, VideoAllProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id','video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']
    class Meta:
        model = VideoAllProxy

admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active = True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)