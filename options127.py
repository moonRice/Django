"""Server Base Settings"""
server_host = '192.168.0.14'
web_run_port = '8000'
allow_all_user_to_use = True

"""Database Settings"""
database_host = '192.168.0.14'
database_port = '3306'
database_username = 'root'
database_password = 'ZDn5AxYcW5BDSa5f'
database_name = 'tongyong'

"""Redis Settings --> Celery"""
redis_celery_server_host = '192.168.0.14'
redis_celery_server_port = '6379'
redis_celery_server_numb = '8'

"""Redis Settings --> Cache"""
redis_cache_server_host = '192.168.0.14'
redis_cache_server_port = '6379'
redis_cache_server_numb = '9'

"""SMTP Server Settings"""
email_host = 'smtp.exmail.qq.com'
email_sender_username = 'admin@per-cloud.cn'
email_sender_password = 'qQ2875623477/'
email_port = 465  # Default = 25
is_use_ssl = True
email_from = '您的激活邮件<admin@per-cloud.cn>'
