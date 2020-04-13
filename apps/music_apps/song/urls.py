"""tongyong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.music_apps.song.views import songsList, SongsDetails

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:zhuanji_id>', views.songsList, name='songs_lists'),
    path('details/<int:song_id>', views.SongsDetails, name='songs_details'),
    # # path('<int:blog_id>', login_required(views.blog_details), name='blog_details'),
]
