from django.contrib import admin
from django.urls import path, include
from .views import indexView, msgShow
from . import views

urlpatterns = [
    path('', indexView.as_view(), name='idx'),
    path('message', msgShow.as_view(), name='msg_show'),
    path('message/<int:blog_id>', views.msgDetails, name='msg_details'),
]
