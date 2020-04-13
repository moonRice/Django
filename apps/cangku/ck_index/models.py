from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.


class types(models.Model):
    name = models.CharField(max_length=255, verbose_name='类型')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_types'
        verbose_name = '仓库主要信息'
        verbose_name_plural = verbose_name


class groups(models.Model):
    name = models.CharField(max_length=255, verbose_name='小组名称')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_groups'
        verbose_name = '小组信息'
        verbose_name_plural = verbose_name


from apps.cangku.ck_yuangong.models import yuangong


class gonggao(models.Model):
    title = models.CharField(max_length=255, verbose_name='公告标题')
    auth = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='发布人')
    context = MDTextField()

    def __str__(self):
        return '%s' % self.title

    class Meta:
        db_table = 'ck_gonggao'
        verbose_name = '公告'
        verbose_name_plural = verbose_name
