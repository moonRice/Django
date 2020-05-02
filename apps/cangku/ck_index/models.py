from django.db import models
from mdeditor.fields import MDTextField
# from db.base_model import BaseModel

# Create your models here.



class types(models.Model):
    name = models.CharField(max_length=255, verbose_name='类型')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_types'
        verbose_name = '类型信息'
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
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    context = MDTextField()

    def __str__(self):
        return '%s' % self.title

    class Meta:
        db_table = 'ck_gonggao'
        verbose_name = '公告'
        verbose_name_plural = verbose_name


class msg(models.Model):
    fjr = models.CharField(max_length=255, verbose_name='发件人')
    sjr = models.ForeignKey(yuangong, on_delete=models.DO_NOTHING, verbose_name='收件人')
    is_read = models.BooleanField(help_text='是否是已读状态', verbose_name='已读消息')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    msg = MDTextField(verbose_name='消息内容')

    def __str__(self):
        return '%s' % self.sjr

    class Meta:
        db_table = 'ck_messages'
        verbose_name = '消息'
        verbose_name_plural = verbose_name
