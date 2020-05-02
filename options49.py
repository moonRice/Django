"""Server Base Settings"""
server_host = '47.100.23.12'
web_run_port = '8000'
allow_all_user_to_use = True

"""Database Settings"""
# database_host = '47.100.23.12'
# database_port = '3306'
# database_username = 'root'
# database_password = 'ZDn5AxYcW5BDSa5f'
# database_name = 'tongyong'


# database_host = '192.168.0.8'
database_host = '192.168.81.129'
database_port = '3306'
database_username = 'root'
database_password = 'root'
#
# # database_name = 'lsgd'
#
database_name = 'tongyong'

"""Redis Settings --> Celery"""
redis_celery_server_host = '47.100.23.12'
redis_celery_server_port = '19985'
redis_celery_server_numb = '5'
redis_celery_server_pass = 'A5mjJTkDmEm8x2ni'

"""Redis Settings --> Cache"""
redis_cache_server_host = '47.100.23.12'
redis_cache_server_port = '19985'
redis_cache_server_numb = '6'
redis_cache_server_pass = 'A5mjJTkDmEm8x2ni'

"""SMTP Server Settings"""
email_host = 'smtp.exmail.qq.com'
email_sender_username = 'admin@per-cloud.cn'
email_sender_password = 'qQ2875623477/'
email_port = 465  # Default = 25
is_use_ssl = True
email_from = '您的激活邮件<admin@per-cloud.cn>'

"""Admin Site Options"""
# \venv\Lib\site-packages\django\contrib\admin\sites.py
my_site_title = '毕设后台管理系统'
my_site_header = '毕设后台管理系统'
my_index_title = '毕设后台管理系统'

"""404 response"""
my_404_errmsg = '你要的页面不见啦~~~【来自django.views.defaults.page_not_found()--line 57】'
