#!/usr/bin/env python
# encoding: utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField,IntegerField,TextAreaField,TextField
from wtforms.validators import Length,InputRequired,regexp,Regexp,EqualTo,Email
from wtforms import Form
from wtforms import ValidationError

class RegisterForm(Form):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱！')])
    password_hash = StringField(validators=[Length(6,15,message='请输入正确格式的密码')])
    password2 = StringField(validators=[EqualTo("password1",message='两次输入的密码不一致！')])
    captcha = StringField(validators=[Length(min=4, max=4, message='请输入正确长度的验证码！')])

    @property
    def password1(self):
        raise ArithmeticError('密码是不可读属性')

    @password1.setter
    def password(self, password1):
       self.password_hash = generate_password_hash(password1)

    def check_password(self, password1):
        return check_password_hash(self.password_hash, password1)

    # def validate_captcha(self,field):
    #     email = self.email.data
    #     captcha = field.data
    #     captcha_cache = cache.get(email)
    #     if not captcha_cache or captcha.lower() != captcha_cache.lower():
    #         raise ValidationError('邮箱验证码错误！')