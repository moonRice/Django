from django.shortcuts import render
from django.views.generic import View

import datetime

from apps.music_apps.sing.models import SingInfo, SingerName, Flag
from apps.music_apps.user_history.models import UserTypeHistory


# Create your views here.


class IndexView(View):
    """音乐推荐"""
    def get(self, request):
        tp_history = UserTypeHistory.objects.order_by('count')
        now_time = datetime.datetime.now()
        return render(request, 'music/index.html', {
            'now_time': now_time,
            'page': 'music',
            'tp_history': tp_history,
        })

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })


class IndexViewDemo(View):
    """音乐推荐【体验版】"""
    def get(self, request):
        tp_history = UserTypeHistory.objects.order_by('-count')
        now_time = datetime.datetime.now()


        singer_li = []
        for singertype in tp_history:
            type = Flag.objects.get(name=singertype.type)
            singer = SingInfo.objects.filter(singer_type=type)
            singer_li.append(singer)

        tools_man = '林俊杰'

        tools_man_information = SingerName.objects.get(name=tools_man)

        tools_man_img = SingInfo.objects.get(singer_name_id=tools_man_information.id)

        context = {
            'now_time': now_time,
            'page': 'music_demo',
            'tools_man_information': tools_man_information,
            'tools_man_img': tools_man_img,
            'tp_history': tp_history,
            'singer_li': singer_li,
        }
        return render(request, 'music/demo/index.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })
