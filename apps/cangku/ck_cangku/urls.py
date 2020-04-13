from django.contrib import admin
from django.urls import path, include
from .views import indexShow

urlpatterns = [
    path('index/', indexShow.as_view(), name='idx')
]
