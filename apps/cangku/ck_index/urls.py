from django.contrib import admin
from django.urls import path, include
from .views import indexView

urlpatterns = [
    path('', indexView.as_view(), name='idx')
]
