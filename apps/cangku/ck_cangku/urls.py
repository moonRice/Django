from django.contrib import admin
from django.urls import path, include
from .views import indexShow, goodslistsShow, goodsdetailsShow, inManage, outManage, ioEchartsView
from . import views

urlpatterns = [
    path('index', indexShow.as_view(), name='idx'),
    path('goodslists', goodslistsShow.as_view(), name='good_list'),
    path('goodsdetails/<int:wp_id>', views.goodsdetailsShow, name='good_detail'),
    path('in', inManage.as_view(), name='in'),
    path('out', outManage.as_view(), name='out'),
    path('ioEcharts', ioEchartsView.as_view(), name='ioe'),
]
