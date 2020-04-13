from django.shortcuts import render
from django.views import View


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
