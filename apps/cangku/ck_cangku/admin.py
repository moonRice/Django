from django.contrib import admin
from .models import yuanqu, cangku, huojia, wupin, dingdan


@admin.register(yuanqu)
class yuanquM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(cangku)
class cangkuM(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'shuliang',
        'forWho',
    )


@admin.register(huojia)
class huojiaM(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'shuliang',
        'forWho',
        'forWhichCangku',
    )


@admin.register(wupin)
class wupinM(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'forWhichHuojia',
    )


@admin.register(dingdan)
class dingdanM(admin.ModelAdmin):
    list_display = (
        'dingdanhao',
        'user',
        'price',
        'is_paid',
    )
