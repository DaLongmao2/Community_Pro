#!/usr/bin/env python
# encoding: utf-8
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# 第三方 初始化
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()

def config_extension(app):
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    # 蓝图
    from APP.user.views import user
    app.register_blueprint(user, url_prefix='')
