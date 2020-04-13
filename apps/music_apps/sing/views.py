from django.shortcuts import render
from django.views.generic import View
from django_redis import get_redis_connection

from .models import SingerName, SingInfo, Flag, Zhuangji
from apps.music_apps.user_history.models import UserTypeHistory

import markdown

# Create your views here.
from ...user.models import User


class singer_list(View):
    def get(self, request):
        # s_l = SingerName.objects.all()
        s_i = SingInfo.objects.all()
        context = {
            # 's_l': s_l,
            's_i': s_i,
        }
        return render(request, 'music/demo/singer_lst.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })


def singer_details(request, singer_id):
    try:
        s_i = SingInfo.objects.get(id=int(singer_id))
    except SingInfo.DoesNotExist:
        return render(request, '404.html' ,{
            'errmsg': '你是不是瞎搞！！！歌手ID不对，赶紧回去重写~'
        })
    s_i.singer_info = markdown.markdown(s_i.singer_info, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.toc',
    ])
    s_t = s_i.singer_type.all()
    user = request.user

    for type in s_t:
        # get_count = 1
        try:
            try:
                user_id = User.objects.get(username=user).id
            except User.DoesNotExist:
                return render(request, '404.html', {
                    'errmsg': '由于分析历史记录需要个人信息，请登录！'
                })
            get_count = UserTypeHistory.objects.get(type=str(type), user_id=user_id).count
        except UserTypeHistory.DoesNotExist:
            get_count = 0

        """若不存在这条记录"""
        if get_count == 0:
            # 1、新数据默认次数为1
            # 2、创建一条新数据，对应填入用户名、类型、次数
            user_type_count = UserTypeHistory.objects.create(user_id=user_id, type=str(type), count=1)
            # 3、写入数据
            user_type_count.save()

        """若存在这条记录"""
        # 1、原有记录基础上加1
        get_count_result = int(get_count) + 1
        # 2、重新定位具体数据
        user_type_count = UserTypeHistory.objects.get(user_id=user_id, type=type)
        # 3、更新数据
        user_type_count.count = get_count_result
        # 4、写入数据
        user_type_count.save()

    s_zj = Zhuangji.objects.filter(auth_id=s_i.id)
    context = {
        's_i': s_i,
        's_t': s_t,
        's_zj': s_zj
    }

    if user.is_authenticated:
        # 添加用户历史浏览记录
        # 1、移除重复记录，并放在第一位作为最新记录
        con = get_redis_connection('default')
        history_key = 'history_%d' % user.id
        # 移除列表中的singer_id
        con.lrem(history_key, 0, singer_id)
        # 并把最新的singer_id左揷
        con.lpush(history_key, singer_id)
        # 只保存用户最新浏览的5条信息
        con.ltrim(history_key, 0, 4)
    else:
        return render(request, '404.html', {
            'errmsg': '由于分析历史记录需要个人信息，请登录！'
        })

    return render(request, 'music/demo/singer_info.html', context)
