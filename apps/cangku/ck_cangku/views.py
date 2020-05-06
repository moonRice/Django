from django.shortcuts import render
from django.views import View
from .models import wupin, cangku, dingdan

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


def dingdanManage(request, sp_id):
    sp_info = wupin.objects.get(id=sp_id)
    user = request.user
    # 获取订单号
    try:
        dd = dingdan.objects.filter(user=user)

    except dingdan.DoesNotExist:
        dingdanhao = '2001'
        baoxian_price = wupin.objects.get(id=sp_id)
        dingdanResult = dingdan.objects.create(user=str(user), dingdanhao=str(dingdanhao), baoxian_id=sp_id,
                                               price=int(baoxian_price.price))
        dingdanResult.save()
        pay_id = dingdan.objects.get(dingdanhao=str(dingdanhao))
        context = {
            'ddh': dingdanhao,
            'price': baoxian_price,
            'sp_info': sp_info,
            'pay_id': pay_id,
        }
        return render(request, 'bx/dingdan.html', context)
    dingdanhao = dingdan.objects.order_by('-dingdanhao')
    d = dingdanhao.first()
    # Ndingdanhao = 0
    Ndingdanhao = int(d.dingdanhao) + 1
    wp_price = wupin.objects.get(id=sp_id).price
    dingdanResult = dingdan.objects.create(user=str(user), dingdanhao=str(Ndingdanhao), baoxian_id=sp_id,
                                           price=wp_price, is_paid='未支付')
    dingdanResult.save()
    is_paid = dingdan.objects.get(dingdanhao=Ndingdanhao).is_paid
    pay_id = dingdan.objects.get(dingdanhao=str(Ndingdanhao))
    context = {
        'ddh': Ndingdanhao,
        'price': wp_price,
        'sp_info': sp_info,
        'is_paid': is_paid,
        'pay_id':pay_id,
    }
    return render(request, 'ck/dingdan.html', context)


class dingdanLists(View):
    def get(self, reqest):
        a = dingdan.objects.order_by('-dingdanhao')
        b = []
        for id in a:
            c = wupin.objects.get(id=id.baoxian_id)
            b.append(c)
        wupin_id = wupin.objects.all()
        count_yzf = dingdan.objects.filter(is_paid='已支付')
        count_wzf = dingdan.objects.filter(is_paid='未支付')
        context = {
            'page': 'ck_dd_list',
            'dd_list': a,
            'count_yzf': count_yzf,
            'count_wzf': count_wzf,
            'sp': b,
            'wupin_id': wupin_id,
        }
        return render(reqest, 'bx/dd_R.html', context)

    def post(self, request):
        pass


def pay(reqest, get_id):
    a = dingdan.objects.get(id=get_id)
    b1 = wupin.objects.get(id=a.baoxian_id).shuliang
    b2 = int(b1) - 1
    c = wupin.objects.get(id=a.baoxian_id)
    c.shuliang = int(b2)
    c.save()
    a.is_paid = '已支付'
    a.save()
    return render(reqest, 'ck/pay.html', {
        'price': a.price,
    })
