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


    # 蓝图
    from APP.user.views import user
    from APP.common.views import common
    app.register_blueprint(user, url_prefix='')
    app.register_blueprint(common, url_prefix='/common')
