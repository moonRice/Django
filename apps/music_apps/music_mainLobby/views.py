from django.shortcuts import render
from django.views.generic import View

import datetime

from apps.music_apps.sing.models import SingInfo, SingerName


# Create your views here.


class IndexView(View):
    """音乐推荐"""
    def get(self, request):
        now_time = datetime.datetime.now()
        return render(request, 'music/index.html', {
            'now_time': now_time,
            'page': 'music',
        })

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })


class IndexViewDemo(View):
    """音乐推荐【体验版】"""
    def get(self, request):
        now_time = datetime.datetime.now()

        tools_man = '林俊杰'

        tools_man_information = SingerName.objects.get(name=tools_man)

        tools_man_img = SingInfo.objects.get(singer_name_id=tools_man_information.id)

        context = {
            'now_time': now_time,
            'page': 'music_demo',
            'tools_man_information': tools_man_information,
            'tools_man_img': tools_man_img,
        }
        return render(request, 'music/demo/index.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })
