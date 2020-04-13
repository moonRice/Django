from django.shortcuts import render
from django.views import View


# Create your views here.


class indexView(View):
    def get(self, request):
        return render(request, 'ck/index.html')

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式错误：POST'
        })
