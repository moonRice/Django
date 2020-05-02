from django.contrib import admin
from django.urls import path, include
from .views import idxView, dataView, dataManage, baoxianManage, dingdanLists
from . import views

urlpatterns = [
    path('index', idxView.as_view(), name='idx'),
    path('baoxian/<int:bx_id>', views.bx_detail, name='bx_detail'),
    path('baoxian/dingdan/<int:bx_id>', views.dingdanManage, name='bx_dingdan'),
    path('dataView', dataView.as_view(), name='data_view'),
    path('dataManage', dataManage.as_view(), name='data_manage'),
    path('baoxianManage', baoxianManage.as_view(), name='baoxian_manage'),
    path('dingdanLists', dingdanLists.as_view(), name='dd_list'),
]
