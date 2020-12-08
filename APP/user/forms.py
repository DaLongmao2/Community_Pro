#!/usr/bin/env python
# encoding: utf-8
from wtforms import StringField,IntegerField,TextAreaField,TextField
from wtforms.validators import Length,InputRequired,regexp,Regexp,EqualTo,Email
from wtforms import Form
from wtforms import ValidationError

from utils.tools import cache


class RegisterForm(Form):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    password1 = StringField(validators=[Length(6,66,message='密码长度为6-66位！')])
    password2 = StringField(validators=[EqualTo("password1",message='两次输入的密码不一致！')])
    captcha = StringField(validators=[Length(min=4, max=4, message='请输入正确长度的验证码！')])

    def validate_captcha(self,field):
        email = self.email.data
        captcha = field.data
        captcha_cache = cache.get(email)
        if not captcha_cache:
            raise ValidationError('验证码输入错误！')
        if not captcha.lower() == captcha_cache.lower():
            raise ValidationError('验证码已过期！')


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式')])
    password = StringField(validators=[Length(6, 66, message='密码长度为6-66位！')])


class ApostForm(Form):
    title = StringField(validators=[InputRequired(message='请输入标题')])
    content = TextField(validators=[InputRequired(message='请输入内容')])