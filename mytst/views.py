from django.shortcuts import render

# Create your views here.
from django.views import View

"""这里是写方法的地方"""
# ok
# 这里开始正式写方法。
# 首先我们要在总控制台那边注册一下我们的app
# 其次在总路由那边注册一下地址
# 注册完，我们再到我们的app这儿接下总路由的大棒
# 顺序错了！应该先写方法！
# 记住下面那个方法
# 这个时候可以跑起来了
# 先看看总路由
# 这个是数据库没连上
class showIndex(View):
    def get(self, request):
        return render(request, 'test/idx.html', {
            'msg': '大家好，我是参数！！！'
        })
    def post(self, request):
        return render(request, 'test/idx.html')
# 做网站的额顺序：
# 1、新建app
# 2、注册app
# 3、注册总路由
# 4、写好view方法
# 5、注册分路由
# 6、网站跑起来！

# 接下来看看你的仓库网站，大致方向我已经订好了