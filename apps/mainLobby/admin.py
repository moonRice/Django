from django.contrib import admin
from . import models
# from .models import pageCtrl, PageName
from .models import Editor


@admin.register(Editor)
class ArticleEditor(admin.ModelAdmin):
    list_display = ('name', 'content')
    # ordering = ('id')


# 新版本用上面的@来注册装饰器
# admin.site.register(Editor, ArticleEditor)

#
# @admin.register(PageName)
# class PageName(admin.ModelAdmin):
#     list_display = ('page_name', 'page_id')
#
#
# @admin.register(pageCtrl)
# class PageCtrl(admin.ModelAdmin):
#     list_display = ('ctrl_user', 'is_open')
