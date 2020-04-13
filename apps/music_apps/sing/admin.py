from django.contrib import admin
from .models import SingInfo, Flag, SingerName, Zhuangji


# Register your models here.
@admin.register(Flag)
class FlagManage(admin.ModelAdmin):
    list_display = (
        'name',
        # 'flag_id',
    )


@admin.register(SingInfo)
class SingerManage(admin.ModelAdmin):
    list_display = (
        'singer_name',
        'singer_info',
    )


@admin.register(SingerName)
class SingerNameManage(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
    )


@admin.register(Zhuangji)
class ZhuanjiManage(admin.ModelAdmin):
    list_display = (
        'name',
        'auth',
    )
