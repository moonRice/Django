from django.db import models
from mdeditor.fields import MDTextField
from apps.cangku.ck_yuangong.models import yuangong


class cangku(models.Model):
    name = models.CharField(max_length=255, verbose_name='仓库名称')
    number = models.CharField(max_length=5, verbose_name='仓库编号')
    shuliang = models.CharField(max_length=5, verbose_name='仓库数量')

    forWho = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='管理方')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_cangku'
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name


class yuanqu(models.Model):
    name = models.CharField(max_length=255, verbose_name='园区名称')
    cangku = models.ManyToManyField(cangku, verbose_name='包含的仓库')
    user = models.ManyToManyField(yuangong, verbose_name='园区负责人')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_yuanqu'
        verbose_name = '园区信息'
        verbose_name_plural = verbose_name


class huojia(models.Model):
    name = models.CharField(max_length=255, verbose_name='货架名称')
    number = models.CharField(max_length=5, verbose_name='货架编号')
    shuliang = models.CharField(max_length=5, verbose_name='货架数量')

    forWho = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='管理方')
    forWhichCangku = models.ForeignKey(cangku, on_delete=models.DO_NOTHING, verbose_name='仓库所属')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_huojia'
        verbose_name = '货架信息'
        verbose_name_plural = verbose_name


class wupin(models.Model):
    name = models.CharField(max_length=255, verbose_name='物品信息')
    price = models.IntegerField(verbose_name='物品价格')
    number = models.CharField(max_length=5, verbose_name='物品编号')
    shuliang = models.CharField(max_length=5, verbose_name='物品数量')
    img = models.CharField(max_length=255, verbose_name='图片链接')
    info = MDTextField(verbose_name='物品介绍')

    forWhichHuojia = models.ForeignKey(huojia, on_delete=models.DO_NOTHING, verbose_name='货架所属')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_wupin'
        verbose_name = '物品信息'
        verbose_name_plural = verbose_name


class dingdan(models.Model):
    user = models.CharField(max_length=255, verbose_name='用户信息')
    dingdanhao = models.CharField(max_length=255, verbose_name='订单号')

    baoxian_id = models.IntegerField(verbose_name='订单内的商品id')
    price = models.IntegerField(verbose_name='订单价格')
    is_paid = models.CharField(max_length=255, verbose_name='是否已经支付')

    def __str__(self):
        return self.dingdanhao

    class Meta:
        db_table = 'ck_dingdan'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
