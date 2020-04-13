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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.user.views import RegisterView, LoginView,LogoutView, ActiveView, UserInfoView, UserAddressView, UserOrderView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),

    # login_required() 登陆装饰器
    # path('', login_required(UserInfoView.as_view()), name='user_center'),
    # path('add', login_required(UserAddressView.as_view()), name='user_addr'),
    # path('ord', login_required(UserOrderView.as_view()), name='user_ord'),

    # Mixin封装，作用和上面的登陆装饰器完全一样，只是更加省事
    path('', UserInfoView.as_view(), name='user_center'),
    path('add', UserAddressView.as_view(), name='user_addr'),
    path('ord', UserOrderView.as_view(), name='user_ord'),
]
