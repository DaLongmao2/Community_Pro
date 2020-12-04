#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for, request

from APP.extension import db
from APP.user.forms import RegisterForm
from APP.user.models import User
from utils import restful
#我的第二个版本
user = Blueprint('user', __name__)


def get_error(form):
    message = form.error.popitem()[1][0]
    return message


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate():
            password=form.password1.data
            email =form.email.data
            e=User.query.filter_by(email=email).first()
            if e:
                return restful.RestfulResult("对不起，该用户名已经存在！")
            user = User(password=password, email=email)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=get_error(form))
    return render_template('user/register.html')


@user.route('/login', methods=['POST', 'GET'])
def login():
    pass


@user.route('/index')
def index():
    return '主页'
