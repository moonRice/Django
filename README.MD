# 基于Django的三大综合平台

------

> 时间：2020年4月13日 星期一 上午11时03分  
>
> 作者：sunRice
>
> 地点：江苏 南京

## 一、概要

​		该综合平台包括以下三大系统：

```python
仓库管理系统

音乐推荐系统

保险销售系统
```



## 二、requirements

​		目前的环境为：

```python
mdeditor
amqp==2.5.2
asgiref==3.2.5
billiard==3.6.3.0
celery==4.4.2
Django==3.0.4
django-redis==4.11.0
django-simpleui==3.9.1
fs-django-mdeditor==0.1.20
itsdangerous==1.1.0
kombu==4.6.8
Markdown==3.2.1
PyMySQL==0.9.3
pytz==2019.3
redis==3.4.1
sqlparse==0.3.1
vine==1.3.0
```



## 三、进度

​		三大平台公用的模块为用户模块，负责用户的注册、登陆。但是，更改密码没有在页面做出，只能登录后在后台管理系统进行更改。

​		用户模块还可以用作各大平台的延伸，譬如说保险系统中客户信息的建立完全基于该用户模块。具体使用方法如下（这里以公司员工信息的建立为例）：

```python
class yuangong(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='账号信息')
    name = models.CharField(max_length=255, verbose_name='员工姓名')
    age = models.CharField(max_length=2, verbose_name='年龄')
    gender = models.BooleanField(verbose_name='性别', help_text='如果是可爱的男孩纸的话，还请勾上哦~')

    groups = models.ManyToManyField(groups, verbose_name='所属小组')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        db_table = 'ck_yuangongInfo'
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name
```

​		其中的user就是关联账号所用，采用`ForeignKey`（一对多）建立联系。

### 1、仓库管理系统

​		已经完成的：

```pyt
1、数据库模型类的设计较为完善

2、数据的操作（完全基于后台管理）
```

​		未完成的：

```pyt
1、数据的可视化

2、数据库的调整
```

​		未来方向：

```pyt
1、借鉴（抄袭？）别人的平台设计
```



### 2、音乐推荐系统

​		已经完成的：

```pyt
1、数据库模型类的设计较为完善

2、数据的操作（完全基于后台管理）
```

​		未完成的：

```pyt
1、数据的可视化

2、推荐系统的实现（基于协同过滤、标签推荐）
```

​		未来方向：

```pyt
1、基于卷积神经网络的协同过滤算法

2、FastBSD分布式存储的实现
```



### 3、保险销售系统

​		已经完成的：

```pyt
1、数据库模型类的设计较为完善

2、无
```

​		未完成的：

```pyt
1、数据的可视化

2、数据库的调整

3、购物车

4、支付系统

5、订单系统

6、评价系统

7、标签推荐
```

​		未来方向：

```pyt
1、
```

