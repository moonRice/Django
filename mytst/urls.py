"""这里是写路由的地方，相当于URL"""
from django.contrib import admin
from django.urls import path, include
from .views import showIndex

urlpatterns = [
    path('', showIndex.as_view(), name='idx')  # 配合反向解析使用
]
