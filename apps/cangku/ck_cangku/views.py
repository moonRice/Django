from django.shortcuts import render
from django.views import View
from .models import wupin, cangku


# Create your views here.


class indexShow(View):
    def get(self, request):
        return render(request, 'ck/cangku.html', {
            'page': 'ck_cangku',
        })

    def poet(self, request):
        return render(request, '404.html', {
            'errmsg': 'POSt请求错误',
        })


class goodslistsShow(View):
    def get(self, request):
        wupin_get = wupin.objects.all()
        context = {
            'page': 'good_list',
            'wp': wupin_get,
        }
        return render(request, 'ck/goodslists.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': 'POSt请求错误',
        })


def goodsdetailsShow(request, wp_id):
    wp_details = wupin.objects.get(id=wp_id)
    context = {
        'page': 'good_list',
        'wp': wp_details,
    }
    return render(request, 'ck/goodsdetails.html', context)


class inManage(View):

    def get(self, request):
        context = {
            'page': 'in',
        }
        return render(request, 'ck/in.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': 'POSt请求错误',
        })


class outManage(View):

    def get(self, request):
        context = {
            'page': 'out',
        }
        return render(request, 'ck/out.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': 'POSt请求错误',
        })


class ioEchartsView(View):

    def get(self, request):
        ck = cangku.objects.all()
        wp = wupin.objects.all()
        context = {
            'page': 'io',
            'ck': ck,
            'wp': wp,
        }
        return render(request, 'ck/ioecharts.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': 'POSt请求错误',
        })
