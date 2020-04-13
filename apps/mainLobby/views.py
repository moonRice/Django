from os import times
import datetime

from django.shortcuts import render, redirect
from django.views.generic import View

# from apps.mainLobby.models import pageCtrl
from apps.user.models import User


# Create your views here.
class IndexView(View):
    def get(self, request):
        now_time = datetime.datetime.now()
        return render(request, 'index.html', {
            'now_time': now_time,
            'page': 'index',
        })

    def post(self, request):
        return render(request, '404.html', {
            'page_name': 'POST_ERROR'
        })


class UpdateInfo(View):
    def get(self, request):
        return render(request, 'update_information.html', {
            'page': 'update'
        })

    def post(self, request):
        return render(request, '404.html')


class ErrorMessage_404(View):
    def get(self, request):
        return render(request, '404.html', {
            'page_name': 'GET_ERROR'
        })

    def post(self, request):
        return render(request, '404.html', {
            'page_name': 'POST_ERROR'
        })
