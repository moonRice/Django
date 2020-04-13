from django.shortcuts import render
from django.views import View
# Create your views here.



class indexShow(View):
    def get(self, request):
        return render(request, 'ck/yuangong.html', {
            'page': 'ck_yuangong'
        })
    def post(self, request):
        return render(request, '404.html', {
            'errmsg': 'post错误请求'
        })