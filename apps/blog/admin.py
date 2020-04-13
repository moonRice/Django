from django.contrib import admin
from .models import MyBlog, BlogType


# Register your models here.
@admin.register(BlogType)
class BlogTypeEditor(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(MyBlog)
class BlogEditor(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create_time', 'update_time')
