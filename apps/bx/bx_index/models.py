from django.db import models

from mdeditor.fields import MDTextField

# Create your models here.
from tongyong import settings


class groups(models.Model):
    name = models.CharField(max_length=255, verbose_name='小组名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bx_groups'
        verbose_name = '小组管理'
        verbose_name_plural = verbose_name


class yuangong_bx(models.Model):
    name = models.CharField(max_length=255, verbose_name='姓名')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='账号信息')

    groups = models.ManyToManyField(groups, verbose_name='所属小组')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bx_yuangong'
        verbose_name = '员工管理'
        verbose_name_plural = verbose_name


class types(models.Model):
    name = models.CharField(max_length=255, verbose_name='种类名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bx_types'
        verbose_name = '种类管理'
        verbose_name_plural = verbose_name


class baoxianInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='保险名称')
    types = models.ManyToManyField(types, verbose_name='保险种类')
    context = MDTextField(verbose_name='保险详情')
    img = models.CharField(max_length=255, verbose_name='图片链接')
    fzr = models.ForeignKey(yuangong_bx, on_delete=models.DO_NOTHING, verbose_name='保险负责人')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bx_Info'
        verbose_name = '保险信息管理'
        verbose_name_plural = verbose_name


class priceManage(models.Model):
    name = models.OneToOneField(baoxianInfo, on_delete=models.DO_NOTHING, verbose_name='保险名称')
    price = models.IntegerField(verbose_name='保险价格')

    class Meta:
        db_table = 'bx_price'
        verbose_name = '保险价格'
        verbose_name_plural = verbose_name


class dingdan(models.Model):
    user = models.CharField(max_length=255, verbose_name='用户信息')
    dingdanhao = models.CharField(max_length=255, verbose_name='订单号')

    baoxian_id = models.IntegerField(verbose_name='订单内的保险id')
    price = models.IntegerField(verbose_name='订单价格')
    is_paid = models.CharField(max_length=255, verbose_name='是否已经支付')

    def __str__(self):
        return self.dingdanhao

    class Meta:
        db_table = 'bx_dingdan_price'
        verbose_name = '订单价格'
        verbose_name_plural = verbose_name
