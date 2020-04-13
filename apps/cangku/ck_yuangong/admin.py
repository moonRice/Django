from django.contrib import admin
from .models import yuangong

# Register your models here.
@admin.register(yuangong)
class yaungongM(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'age',
        'gender',
    )