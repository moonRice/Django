# 使用celery
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

import options49

# 初始化
# 在任务处理端加入初始化代码
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tongyong.settings')
django.setup()

# 创建一个celery类的实例对象
app = Celery('celery_tasks.tasks',
             broker='redis://:' + options49.redis_celery_server_pass + '@' + options49.redis_celery_server_host + ':' + options49.redis_celery_server_port + '/' + options49.redis_celery_server_numb)


# 定义任务函数
@app.task
def send_register_active_mail(to_email, username, token):
    '''发送激活邮件'''
    subject = '【在线仓库】激活邮件'
    message = ''
    from_email = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s，欢迎您！</h1>请点击以下链接激活您的账号：<br/><a ''href="http://47.100.23.12:8000/user/active/%s">前往激活...</a>' % (username, token)

    send_mail(subject, message, from_email, receiver, html_message=html_message)  # html_message必须这样写，他不是第五个参数
