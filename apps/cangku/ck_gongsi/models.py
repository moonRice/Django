from django.db import models
from apps.cangku.ck_index.models import types
from apps.cangku.ck_yuangong.models import yuangong


# Create your models here.


class gongsi(models.Model):
    name = models.CharField(max_length=255, verbose_name='公司名称')

    types = models.ManyToManyField(types, verbose_name='公司类型')
    yuangong = models.ManyToManyField(yuangong, verbose_name='员工信息')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_gongsiInfo'
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name
