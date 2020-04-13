from django.db import models
from db.base_model import BaseModel
from django.conf import settings


# Create your models here.


class UserTypeHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='用户名')

    count = models.IntegerField(verbose_name='类型点击次数')
    type = models.CharField(max_length=255, verbose_name='类型')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'ty_UserTypeHistoryCount'
        verbose_name = '用户类型点击计数'
        verbose_name_plural = verbose_name


class UserLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='用户名')

    result = models.CharField(max_length=255, verbose_name='推荐的类型')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'ty_UserLike'
        verbose_name = '推荐给用户的类型'
        verbose_name_plural = verbose_name
