from django.contrib import admin
from .models import types, baoxianInfo

# Register your models here.
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