#!/usr/bin/env python
# encoding: utf-8




DEBUG = False
TESTING = False
SECRET_KEY = "wertyuiodfghjkl!@#$%^&I(*&^5"

# 数据库配置
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 谷歌验证码
# RECAPTCHA_PUBLIC_KEY = '6LewDfEZAAAAAIQ2YFdbPjdzzpC4clmOOs3YBpUZ'
# RECAPTCHA_PRIVATE_KEY = '6LewDfEZAAAAAOM6FqE37AJqCmjTKvbnvX5Dq4qj'

# 邮件配置
# 服务器ip地址
MAIL_SERVER = "smtp.qq.com"
# 端口号:TLS对应587,SSL对应465
MAIL_PORT = "587"
MAIL_USE_TLS = True
# 默认发送者
MAIL_DEFAULT_SENDER = "dalongmao.zhang@qq.com"
# 发送者邮箱
MAIL_USERNAME = "dalongmao.zhang@qq.com"
MAIL_PASSWORD = "ohhvvhwltfovbgac"

# radise
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1122@localhost:3306/community"

def init_app(app):
    pass

