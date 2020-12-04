#!/usr/bin/env python
# encoding: utf-8
import random
import string
from flask import Blueprint, render_template, redirect, url_for, request
import re
from task import send_mail
from utils import restful
from utils.tools import cache

common = Blueprint('common', __name__)


@common.route('/send_captcha/')
def send_captcha():
    print('执行了')
    email = request.args.get('email')
    ret = re.match(r'^.+@([^.@][^@]+)$', email)
    if ret:
        E = list(string.ascii_letters)
        E.extend(map(lambda x: str(x), range(0, 10)))
        cap = ''.join(random.sample(E,4))

        text = f'您的验证码是：\n {cap} \n打死也别告诉别人哦~~\n有效期为5分钟'

        print(email, cap, text)
        try:
           send_mail.delay([email], '注册验证码', text)
        except:
            return restful.server_error()
        cache.set(email, cap, ex=300)
        return restful.success()
    else:
        return restful.params_error("邮箱不存在！")


@common.route('/t/')
def t():
    send_mail.delay(['872039610@qq.com'], '验证码', 'dsf第三方')
    return 'ok'