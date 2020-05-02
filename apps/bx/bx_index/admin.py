from django.contrib import admin
from .models import types, baoxianInfo, yuangong_bx, groups, priceManage, dingdan


# Register your models here.


@admin.register(groups)
class groupsM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(yuangong_bx)
class yuangong_bxM(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
    )


@admin.register(types)
class typesM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(baoxianInfo)
class bcM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(priceManage)
class priceM(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


@admin.register(dingdan)
class dingdanM(admin.ModelAdmin):
    list_display = (
        'dingdanhao',
        'user',
        'price',
        'is_paid',
    )
