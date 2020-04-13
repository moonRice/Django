from django.shortcuts import render
from django.views import View


# Create your views here.


class idxView(View):
    def get(self, request):
        return render(request, 'bx/idx.html')

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })
