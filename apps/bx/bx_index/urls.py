from django.contrib import admin
from django.urls import path, include
from .views import idxView

urlpatterns = [
    path('index', idxView.as_view(), name='idx')
]
