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

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('apps.user.urls', 'user'), namespace='user')),
    path('', include(('apps.mainLobby.urls', 'mainLobby'), namespace='mainLobby')),

    path('mdeditor/', include('mdeditor.urls')),
    path('blog/', include(('apps.blog.urls', 'MyBlog'), namespace='MyBlog')),

    # 音乐平台
    path('music/', include(('apps.music_apps.music_mainLobby.urls', 'music'), namespace='music')),
    path('singer/', include(('apps.music_apps.sing.urls', 'singer'), namespace='singer')),
    path('songs/', include(('apps.music_apps.song.urls', 'songs'), namespace='songs')),

    # 仓库平台
    path('cangku/', include(('apps.cangku.ck_index.urls', 'cangku'), namespace='cangku')),
    path('ck/', include(('apps.cangku.ck_cangku.urls', 'ck_cangku'), namespace='ck_cangku')),
    path('yg/', include(('apps.cangku.ck_yuangong.urls', 'ck_yuangong'), namespace='ck_yuangong')),
    # 保险销售
    path('bx/', include(('apps.bx.bx_index.urls', 'baoxian'), namespace='baoxian')),

    path('ceshi/', include(('mytst.urls', 'ceshi'), namespace='ceshi'))  # namespace是反向解析
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)