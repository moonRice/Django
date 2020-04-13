from django.db import models
from db.base_model import BaseModel
from apps.music_apps.sing.models import Flag, SingInfo, Zhuangji

from mdeditor.fields import MDTextField


# Create your models here.
class SongInfo(models.Model):
    song_name = models.CharField(max_length=100, verbose_name='歌曲名称')
    song_type = models.ManyToManyField(Flag, verbose_name='歌曲标签')
    song_list = models.ForeignKey(Zhuangji, on_delete=models.DO_NOTHING, verbose_name='所属专辑')
    # image = models.ImageField(upload_to='images', verbose_name='图片链接')
    image = models.CharField(max_length=255, verbose_name='图片链接')

    song_auth = models.ForeignKey(SingInfo, on_delete=models.DO_NOTHING, verbose_name='唱曲人')

    def __str__(self):
        return '歌曲：%s' % self.song_name

    class Meta:
        db_table = 'ty_Song_Info'
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name


class SongList(BaseModel):
    list_name = models.CharField(max_length=100, verbose_name='歌单信息')
    list_type = models.ManyToManyField(Flag, verbose_name='歌单标签')
    list_songs = models.ManyToManyField(SongInfo, verbose_name='歌单列表')
    image_URL = models.CharField(max_length=255, verbose_name='图片链接')
    list_info = MDTextField(verbose_name='歌单信息')

    def __str__(self):
        return '歌单：%s' % self.list_name

    class Meta:
        db_table = 'ty_List_Info'
        verbose_name = '歌单信息'
        verbose_name_plural = verbose_name


class iFrameM(models.Model):
    url = models.CharField(max_length=255, verbose_name='内嵌框架')

    song = models.ForeignKey(SongInfo, on_delete=models.DO_NOTHING, verbose_name='歌曲名')

    def __str__(self):
        return '%s' % self.song

    class Meta:
        db_table = 'ty_iframe'
        verbose_name = '内嵌框架管理'
        verbose_name_plural = verbose_name