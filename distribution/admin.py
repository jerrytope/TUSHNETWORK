from django.contrib import admin
from .models import Release, Track, Platform, Distribution

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'release_type', 'status', 'release_date')
    list_filter = ('release_type', 'status', 'genre')
    search_fields = ('title', 'artist_name')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'release', 'track_number', 'duration')

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('release', 'platform', 'is_distributed', 'distributed_at')