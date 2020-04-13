from django.contrib import admin
from .models import cangku, huojia


@admin.register(cangku)
class cangkuM(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'forWho',
    )


@admin.register(huojia)
class huojiaM(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'forWho',
    )
