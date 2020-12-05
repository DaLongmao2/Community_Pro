#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from APP.extension import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), default='新用户...')
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    activation = db.Column(db.Boolean, default=False)
    gender = db.Column(db.String(10), default='秘密')
    signature = db.Column(db.Text, default='这家伙很懒，什么都没有留下~')
    avatar = db.Column(db.String(300), default="https://donghaocms.oss-cn-beijing.aliyuncs.com/avater/default.jpg")

    # 保护字段
    @property
    def password(self):
        raise ArithmeticError("密码是不可读属性")

    #　生成hash
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    #
    # # 生成 token
    # def generate_token(self):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_in=current_app.config['EXPIRES_IN_TOKEN'])
    #     return s.dumps({'id': self.id})
    #
    # #　校验
    # @staticmethod
    # def check_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #     except:
    #         return False
    #     user = User.query.get(data.get('id'))
    #     if user is None:
    #         return False
    #     if not user.activation:
    #         user.activation = True
    #         db.session.add(user)
    #     return True