from django.db import models
from db.base_model import BaseModel

from mdeditor.fields import MDTextField


# Create your models here.
class Flag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名称')

    # flag_id = models.IntegerField(verbose_name='标签编号')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ty_Music_Type'
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name


class SingerName(models.Model):
    name = models.CharField(max_length=255, verbose_name='歌手姓名')
    gender = models.CharField(max_length=8, verbose_name='歌手性别')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ty_SingerName'
        verbose_name = '歌手姓名'
        verbose_name_plural = verbose_name


class SingInfo(models.Model):
    singer_name = models.ForeignKey(SingerName, on_delete=models.DO_NOTHING, verbose_name='歌手姓名')
    singer_type = models.ManyToManyField(Flag, verbose_name='歌手标签')
    image_URL = models.CharField(max_length=255, verbose_name='头像')

    singer_info = MDTextField(verbose_name='歌手简介')

    def __str__(self):
        return '%s' % self.singer_name

    class Meta:
        db_table = 'ty_Sing_Info'
        verbose_name = '歌手信息'
        verbose_name_plural = verbose_name


class Zhuangji(models.Model):
    name = models.CharField(max_length=255, verbose_name='专辑名称')
    auth = models.ForeignKey(SingInfo, on_delete=models.DO_NOTHING, verbose_name='专辑作者')
    image_URL = models.CharField(max_length=255, verbose_name='专辑配图链接')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ty_Zhuangji'
        verbose_name = '专辑信息'
        verbose_name_plural = verbose_name


