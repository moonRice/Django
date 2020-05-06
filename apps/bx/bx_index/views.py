from django.shortcuts import render
from django.views import View
from .models import yuangong_bx, types, priceManage, groups, baoxianInfo, dingdan
from apps.user.models import User


# Create your views here.


class idxView(View):
    def get(self, request):
        bxInfo = baoxianInfo.objects.all()
        bxPrice = priceManage.objects.all()
        context = {
            'page': 'bx_idx',
            'bxInfo': bxInfo,
            'bxPrice': bxPrice,
        }
        return render(request, 'bx/idx.html', context)

    def post(self, request):
        return render(request, '404.html', {
            'errmsg': '请求方式POST错误！'
        })


def bx_detail(request, bx_id):
    bxInfo = baoxianInfo.objects.get(id=bx_id)
    bxTypes = bxInfo.types.all()
    bxPrice = priceManage.objects.get(name_id=bx_id)
    context = {
        'page': 'bx_idx',
        'bxInfo': bxInfo,
        'bxTypes': bxTypes,
        'bxPrice': bxPrice,
    }
    return render(request, 'bx/baoxiandetails.html', context)


def dingdanManage(request, bx_id):
    bc_info = baoxianInfo.objects.get(id=bx_id)
    user = request.user
    # 获取订单号
    try:
        dd = dingdan.objects.filter(user=user)

    except dingdan.DoesNotExist:
        dingdanhao = '2001'
        baoxian_price = priceManage.objects.get(name_id=bx_id)
        dingdanResult = dingdan.objects.create(user=str(user), dingdanhao=str(dingdanhao), baoxian_id=bx_id,
                                               price=int(baoxian_price.price))
        dingdanResult.save()
        pay_id = dingdan.objects.get(dingdanhao=str(dingdanhao))
        context = {
            'ddh': dingdanhao,
            'price': baoxian_price,
            'bc_info': bc_info,
            'pay_id': pay_id,
        }
        return render(request, 'bx/dingdan.html', context)
    dingdanhao = dingdan.objects.order_by('-dingdanhao')
    d = dingdanhao.first()
    # Ndingdanhao = 0
    Ndingdanhao = int(d.dingdanhao) + 1
    baoxian_price = priceManage.objects.get(name_id=bx_id).price
    dingdanResult = dingdan.objects.create(user=str(user), dingdanhao=str(Ndingdanhao), baoxian_id=bx_id,
                                           price=baoxian_price, is_paid='未支付')
    dingdanResult.save()
    is_paid = dingdan.objects.get(dingdanhao=Ndingdanhao).is_paid
    pay_id = dingdan.objects.get(dingdanhao=str(Ndingdanhao))
    context = {
        'ddh': Ndingdanhao,
        'price': baoxian_price,
        'bc_info': bc_info,
        'is_paid': is_paid,
        'pay_id': pay_id,
    }
    return render(request, 'bx/dingdan.html', context)


class dataView(View):
    def get(self, reqest):
        context = {
            'page': 'bx_data_view',
        }
        return render(reqest, 'bx/dataView.html', context)

    def post(self, request):
        pass


class dataManage(View):
    def get(self, reqest):
        context = {
            'page': 'bx_data_manage',
        }
        return render(reqest, 'bx/dataManage.html', context)

    def post(self, request):
        pass


class baoxianManage(View):
    def get(self, reqest):
        context = {
            'page': 'bx_baoxian_manage',
        }
        return render(reqest, 'bx/baoxianManage.html', context)

    def post(self, request):
        pass


class dingdanLists(View):
    def get(self, reqest):
        a = dingdan.objects.order_by('-dingdanhao')
        b = []
        for id in a:
            c = baoxianInfo.objects.get(id=id.baoxian_id)
            b.append(c)
        wupin_id = baoxianInfo.objects.all()
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


class baoxianManage(View):
    def get(self, reqest):
        context = {
            'page': 'bx_baoxian_manage',
        }
        return render(reqest, 'bx/baoxianManage.html', context)

    def post(self, request):
        pass


def pay(reqest, id):
    a = dingdan.objects.get(id=id)
    a.is_paid = '已支付'
    a.save()
    return render(reqest, 'bx/pay.html', {
        'price': a.price,
    })
