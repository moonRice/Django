from django.db import models

from mdeditor.fields import MDTextField


# Create your models here.
from tongyong import settings


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
    fzr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='保险负责人')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bx_Info'
        verbose_name = '保险信息管理'
        verbose_name_plural = verbose_name
