#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for, request, session, g
from jinja2.filters import do_striptags

from APP import config
from APP.extension import db
from APP.user.forms import RegisterForm, LoginForm, ApostForm
from APP.user.models import UserModel, TagsModel, PostsModel
from utils import restful, safeurls

user = Blueprint('user', __name__)


@user.before_request
def before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = UserModel.query.get(user_id)
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
        form = RegisterForm(request.form)
        if form.validate():
            password = form.password1.data
            email = form.email.data
            print(password, email)
            e = UserModel.query.filter_by(email=email).first()
            print(e)
            if e:
                return restful.params_error("对不起，该邮箱已经存在！")
            else:
                user = UserModel(password=password, email=email)
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
            user = UserModel.query.filter_by(email=email).first()
            print(user)
            if not user:
                return restful.params_error(message='邮箱不存在')
            if not user.is_active:
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
    return 'pass'


# TODO： 登录保护
@user.route('/apost/',methods=['GET','POST'])
def apost():
    if request.method == 'GET':
        return render_template('user/apost.html')
    else:
        tags = request.form.get('tags')
        form = ApostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            tags = tags.split(',')
            all_tags = TagsModel.query.all()
            all_tagnames = [tag.tagname for tag in all_tags]
            post = PostsModel(title=title, content=content)
            post.author = g.user
            for tag in tags:
                if tag in all_tagnames:
                    ta = TagsModel.query.filter_by(tagname=tag).first()
                else:
                    ta = TagsModel(tagname=tag)
                post.tags.append(ta)

            charactors_len = len(do_striptags(post.content))
            post.author.points += 2
            print(charactors_len)
            print(type(charactors_len))
            post.author.charactors = charactors_len
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='格式错误')
