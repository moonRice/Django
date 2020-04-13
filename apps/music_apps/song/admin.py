from django.contrib import admin
from .models import SongInfo, SongList, iFrameM


# Register your models here.
@admin.register(SongInfo)
class SongManage(admin.ModelAdmin):
    list_display = (
        'song_name',
        'song_auth',
        'song_list',
    )


@admin.register(SongList)
class SongListManage(admin.ModelAdmin):
    list_display = (
        'list_name',
        'list_info',
    )


@admin.register(iFrameM)
class iFManage(admin.ModelAdmin):
    list_display = (
        'song',
        'url',
    )