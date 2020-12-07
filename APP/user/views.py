#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for, request, session, g

from APP import config
from APP.extension import db
from APP.user.forms import RegisterForm, LoginForm
from APP.user.models import User
from utils import restful, safeurls

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    print('我只醒了')
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = User.query.get(user_id)
        if user:
            g.user = user
    else:
        g.user = ''


def get_error(form):
    message = form.errors.popitem()
    return message


@user.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # print(g.user)
        # user = User.query.order_by(User.ch)
        return render_template('user/base.html')


@user.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        print(request.form)
        form = RegisterForm(request.form)
        print(form)
        if form.validate():
            password = form.password1.data
            email = form.email.data
            print(password, email)
            e = User.query.filter_by(email=email).first()
            print(e)
            if e:
                return restful.params_error("对不起，该邮箱已经存在！")
            else:
                user = User(password=password, email=email)
                db.session.add(user)
                db.session.commit()
                return restful.success()
        else:
            return restful.params_error()
    return render_template('user/register.html')


@user.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        #  获取哪里进来的连接
        # http://127.0.0.1:5000/register/
        return_to = request.referrer
        if return_to and return_to != request.url and safeurls.is_safe_url(return_to):
            return render_template("user/login.html", return_to=return_to)
        else:
            return render_template("user/login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.email.data
            user = User.query.filter_by(email=email).first()
            print(user)
            if not user:
                return restful.params_error(message='邮箱不存在')
            if not user.activation:
                return restful.params_error(message="您的账户已经被冻结！请联系管理员！")
            if not user and user.check_password(password):
                return restful.params_error('密码错误')
            else:
                session[config.FRONT_USER_ID] = user.id
                return restful.success()
        else:
            return restful.params_error('用户不存在')


@user.route('/forgot_password/')
def forgot_password():
    return "忘记密码"


@user.route('/login_out/')
def login_out():
    return "登出"



