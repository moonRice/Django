from django.db import models
from mdeditor.fields import MDTextField
from db.base_model import BaseModel
# from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='文章类型')

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'ty_MyBlogType'
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class MyBlog(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    content = MDTextField(verbose_name='文章内容')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='文章类型')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='作者')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    def __str__(self):
        return '文章：%s' % self.title

    class Meta:
        db_table = 'ty_MyBlog'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
