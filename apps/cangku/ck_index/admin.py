from django.contrib import admin
from .models import types, groups, gonggao, msg


# Register your models here.
@admin.register(types)
class typesM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(groups)
class groupsM(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(gonggao)
class gonggaoM(admin.ModelAdmin):
    list_display = (
        'title',
        'auth',
    )


@admin.register(msg)
class msgM(admin.ModelAdmin):
    list_display = (
        'sjr',
        'fjr',
        'is_read',
        'create_time',
    )
