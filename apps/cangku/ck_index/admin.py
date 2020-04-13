from django.contrib import admin
from .models import types, groups, gonggao


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
