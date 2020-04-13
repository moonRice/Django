import re

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View

from apps.user.models import User, Address
from django.contrib.auth import authenticate, login, logout
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired

# from django.core.mail import send_mail
from celery_tasks.tasks import send_register_active_mail as sendMail

from django.shortcuts import render, redirect
from django.conf import settings

from utils.mixin import LoginRequiredMixin as loMxi

# Django自带的
from django_redis import get_redis_connection

from apps.music_apps.song.models import SongInfo
from apps.music_apps.sing.models import SingerName, SingInfo

import options49

from apps.music_apps.user_history.models import UserTypeHistory, allHistoryCount


# Create your views here.
class LoginView(View):
    """Show Login Website"""

    def get(self, request):
        """Get --> Show Login Website"""
        # 判断是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {
            'username': username,
            'checked': checked
        })

    def post(self, request):
        """Post -- > Ready To Login"""
        # return render(request, '404.html')
        # return redirect(reverse('mainLobby:index'))

        # Get The Data From 'login.html'
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not all(
                [
                    username,
                    password
                ]
        ):
            return render(request, 'login.html', {
                'username_errmsg': '用户名不能为空！',
                'password_errmsg': '密码不能为空',
                'errmsg': '你瞅瞅，连格儿都填不满，咋会四啊小老弟~'
            })

        user_check = authenticate(username=username, password=password)
        if user_check is not None:
            if user_check.is_active:
                # 用户已激活
                # 记录用户的登陆状态
                # 天坑！！！！！！！
                # 未激活用户依旧返回None
                # 详见settings解决方案
                login(request, user_check)

                # 登陆装饰器
                # 获取登陆后所要跳转的地址
                next_URL = request.GET.get('next', reverse('mainLobby:index'))  # 第二个参数是默认跳转值
                # 假若这个人故意删除next后面的地址，则next_URL = None
                # 后面的response就会报错
                # 所以在最后要设置默认跳转，以防小人捣乱

                # 跳转到接收到的next值
                response = redirect(next_URL)

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')

                if remember == 'on':
                    # 记住用户名
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                return response

                # return redirect(reverse('mainLobby:index'))
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '账号莫有激活！你就不能瞅瞅你那邮箱里的激活邮件~'})
        else:
            return render(request, 'login.html', {'errmsg': '用户名和密码皆错误！也不晓得你是咋填滴~'})


# /user/logout
class LogoutView(View):
    """Logout Vies"""

    def get(self, request):
        """Exit"""
        """Clear User's Session"""
        logout(request)

        """Jump To Index"""
        return redirect(reverse('mainLobby:index'))


class RegisterView(View):
    """注册类"""

    def get(self, request):
        """显示注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """进行注册"""
        # return render(request, '404.html')

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all(
                [
                    username,
                    password,
                    email
                ]
        ):
            return render(request, 'register.html', {
                'errmsg': '请检查你的信息填写情况！',
                'username_errmsg': '用户名不能为空！',
                'password_errmsg': '密码不能为空！',
                'email_errmsg': '邮箱不能为空',
                'allow_errmsg': '必须认可我们的用户协议！',
                'color_username': 'red',
                'color_password': 'red',
                'color_email': 'red',
                'color_allow': 'red'
            })
        if not re.match('[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {
                'email_errmsg': '邮箱格式不对',
                'color_email': 'red'
            })
        if allow != 'on':
            return render(request, 'register.html', {
                'allow_errmsg': '必须认可我们的用户协议！',
                'color_allow': 'red'
            })
        if len(username) > 21 or len(username) < 5:
            return render(request, 'register.html', {
                'username_errmsg': '用户名长度必须在6~20个字符之间',
                'color_username': 'red'
            })
        if len(password) > 21 or len(password) < 5:
            return render(request, 'register.html', {
                'password_errmsg': '密码长度必须在6~20个字符之间',
                'color_password': 'red'
            })

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        user_register = User.objects.create_user(username, email, password)
        user_register.is_active = 0
        user_register.save()

        ser = Serializer(settings.SECRET_KEY, 300)
        info = {
            'confirm': user_register.id
        }
        token = ser.dumps(info)
        token = token.decode('UTF8')

        # subject = '注册激活欢迎信息'
        # message = ''
        # from_email = settings.EMAIL_FROM
        # receiver = [email]
        # html_message = '<h1>%s，欢迎您成为预注册会员！</h1>请点击以下链接激活您的账号：<br/><a ' \
        #                'href="http://localhost:8000/user/active/%s">前往激活...</a>' % (
        #                    username, token)
        #
        # send_mail(subject, message, from_email, receiver, html_message=html_message)  # html_message必须这样写，他不是第五个参数
        sendMail.delay(email, username, token)

        return redirect(reverse('user:login'))


class ActiveView(View):
    def get(self, request, token):
        ser = Serializer(settings.SECRET_KEY, 300)
        # 导入异常
        try:
            info = ser.loads(token)
            # 获取待激活用户ID
            user_id = info[
                'confirm'
            ]
            # 根据ID获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 返回应答，跳转到登录页面【反向解析】namespace:name
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            # 激活链接已过期
            return HttpResponse('激活链接已过期！')


# /user
class UserInfoView(loMxi, View):
    """User Center"""

    def get(self, request):
        """show page"""
        # request.user.is_authenticated()
        # 除了你给模板文件传递的模板变量之外，Django框架会把request.user也传给模板文件
        # 倘若用户未登录 --> AnonymousUser类的一个实例
        # 倘若用户登录 --> User类的一个实例

        # 返回用户注册的基本信息
        user = request.user
        address = Address.objects.get_default_address(user)

        # 获取相关商品信息【记录、商品相关联】
        # 从数据库中查询
        # 要导入物品信息modle类

        return render(request, 'user_center.html', {
            'address': address,
        })


# /user/order
class UserOrderView(loMxi, View):
    """User Center"""

    def get(self, request):
        """show User's View Logs"""
        user = request.user
        # 获取用户历史浏览记录
        from redis import StrictRedis
        # sr = StrictRedis(host=options49.redis_cache_server_host, port=options49.redis_cache_server_port,
        # db=options49.redis_cache_server_numb) 由于django自带【StrictRedis的实例对象】
        con = get_redis_connection('default')

        # 取出历史记录
        history_key = 'history_%d' % user.id

        # 获取用户最新浏览的5条记录
        new_history_ids = con.lrange(history_key, 0, 4)
        # 此时会返回一个列表
        # songs_li = SongInfo.objects.filter(id_in=sku_ids)

        # 从数据库中查询用户浏览的商品的具体信息
        # sings_li = SingInfo.objects.filter(id__in=new_history_ids)

        # 遍历获取用户历史浏览记录

        sings_li = []
        for id in new_history_ids:
            sings = SingInfo.objects.get(id=id)
            sings_li.append(sings)

        # 返回图表数据————点击计数
        flag = '2'
        a = None
        b = None
        flagR = None
        userID = User.objects.get(username=user).id
        allUser = User.objects.all()
        try:
            a = UserTypeHistory.objects.filter(user_id=userID)
        except UserTypeHistory.DoesNotExist:
            flag = '0'
            flagR = '0'

        if flag == '2':
            a = UserTypeHistory.objects.filter(user_id=userID)
            b = allHistoryCount.objects.all()
            flagR = '1'
        # 组织上下文
        context = {
            'sings_li': sings_li,
            'r': a,
            'b': b,
            'flagR': flagR,
            'allUser': allUser,
        }

        return render(request, 'user_ord.html', context)


class UserAddressView(loMxi, View):
    """User Center"""

    def get(self, request):
        """show page"""
        # 获取登录用户对应的user对象
        user = request.user
        # 获取用户的默认地址【已经放到models.py里面】
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在收货地址
        #     address = None
        address = Address.objects.get_default_address(user)

        if address == None:
            return render(request, 'user_add.html', {
                'addr': None,
            })
        else:
            # 使用模板的时候传参
            return render(request, 'user_add.html', {
                'addr': address,
            })

    def post(self, request):
        """Add address"""

        """从前端获取数据"""
        sjr = request.POST.get('sjr')
        xxdz = request.POST.get('xxdz')
        yb = request.POST.get('yb')
        lxdh = request.POST.get('lxdh')

        """校验数据"""
        if not all(
                [
                    sjr,
                    xxdz,
                    lxdh,
                ]
        ):
            return render(request, 'user_add.html', {
                'err_msg': '信息不完整',
            })

        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', lxdh):
            return render(request, 'user_add.html', {
                'color_lxdh': 'red',
                'err_msg': '联系电话格式错误'
            })

        """业务处理 ——》 地址添加"""
        # 倘若用户已经存在默认收货地址，那么新添加的地址将不会替换原先的默认收货地址
        # 获取登录用户对应的user对象
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在收货地址
        #     address = None
        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(user=user, addr=xxdz, receiver=sjr, zip_code=yb, phone=lxdh, is_default=is_default)

        """返回应答"""
        # 刷新地址页面
        return redirect(reverse('user:user_addr'))  # GET请求方式