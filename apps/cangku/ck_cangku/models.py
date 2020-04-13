from django.db import models

from apps.cangku.ck_yuangong.models import yuangong


class cangku(models.Model):
    name = models.CharField(max_length=255, verbose_name='仓库名称')
    number = models.CharField(max_length=5, verbose_name='仓库编号')

    forWho = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='管理方')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_cangkuInfo'
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name


class huojia(models.Model):
    name = models.CharField(max_length=255, verbose_name='货架名称')
    number = models.CharField(max_length=5, verbose_name='货架编号')

    forWho = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='管理方')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_cangkuInfo'
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name
