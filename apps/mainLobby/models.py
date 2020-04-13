from django.db import models
from mdeditor.fields import MDTextField

from django.conf import settings


class Editor(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()

    def __str__(self):
        return '文章标题:%s' % self.name
#
#
# class PageName(models.Model):
#     """页面名称"""
#     page_name = models.CharField(max_length=25, verbose_name='页面名称')
#     page_id = models.IntegerField(verbose_name='页面编号')
#
#     def __str__(self):
#         return self.page_name
#
#     class Meta:
#         db_table = 'ty_pageName'
#         verbose_name = '页面名称管理'
#         verbose_name_plural = verbose_name
#
#
# class pageCtrl(models.Model):
#     """页面控制"""
#     is_open = models.BooleanField(verbose_name='是否可以访问')
#     ctrl_page_name = models.ManyToManyField(PageName, verbose_name='受控制的页面名称')
#     ctrl_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='受控人')
#
#     def __str__(self):
#         return self.ctrl_page_name
#
#     class Meta:
#         db_table = 'ty_pageCtrl'
#         verbose_name = '页面访问控制'
#         verbose_name_plural = verbose_name
