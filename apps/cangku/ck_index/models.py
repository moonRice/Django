from django.db import models


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
