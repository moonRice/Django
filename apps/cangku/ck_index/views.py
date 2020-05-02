from django.shortcuts import render
from django.views import View
from apps.cangku.ck_cangku.models import yuanqu, cangku, huojia
from .models import gonggao, groups, msg


# Create your views here.


class indexView(View):
    def get(self, request):
        yuanqu_get = yuanqu.objects.all()
        cangku_get = cangku.objects.all()
        huojia_get = huojia.objects.all()
        gonggao_get = gonggao.objects.all()
        groups_get = groups.objects.all()

        context = {
            'page': 'cangku',
            'yuanqu_get': yuanqu_get,
            'cangku_get': cangku_get,
            'huojia_get': huojia_get,
            'gonggao_get': gonggao_get,

            'groups_get': groups_get,
        }

        return render(request, 'ck/index.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式错误：POST'
        })


class msgDetails(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class msgShow(View):
    def get(self, request):
        return render(request, 'ck/msg_list.html')

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式错误：POST'
        })
