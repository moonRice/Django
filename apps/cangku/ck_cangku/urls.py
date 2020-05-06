from django.contrib import admin
from django.urls import path, include
from .views import indexShow, goodslistsShow, inManage, outManage, ioEchartsView, dingdanLists
from . import views

urlpatterns = [
    path('index', indexShow.as_view(), name='idx'),
    path('goodslists', goodslistsShow.as_view(), name='good_list'),
    path('goodsdetails/<int:wp_id>', views.goodsdetailsShow, name='good_detail'),
    path('in', inManage.as_view(), name='in'),
    path('out', outManage.as_view(), name='out'),
    path('ioEcharts', ioEchartsView.as_view(), name='ioe'),

    path('baoxian/dingdan/<int:sp_id>', views.dingdanManage, name='dingdan'),
    path('dingdanLists', dingdanLists.as_view(), name='dd_list'),

    path('pay/<int:get_id>', views.pay, name='pay'),
]
