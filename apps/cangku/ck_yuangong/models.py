from django.db import models
from apps.cangku.ck_index.models import groups


# Create your models here.
from tongyong import settings


class yuangong(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='账号信息')
    name = models.CharField(max_length=255, verbose_name='员工名称')
    age = models.CharField(max_length=2, verbose_name='年龄')
    gender = models.BooleanField(verbose_name='性别')

    groups = models.ManyToManyField(groups, verbose_name='所属小组')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_yuangongInfo'
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name
