#!/usr/bin/env python
# encoding: utf-8
from flask import current_app, render_template
from flask_mail import Message
from APP.extension import mail
from threading import Thread

# 发送 邮件需要程序的上下文 否则不能发送
def async_send_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    # 从current_app 对象中获取的原始实例
    app = current_app._get_current_object()
    msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)
    # msg.body = render_template(template + '.txt', **kwargs)
    thr = Thread(target=async_send_email, args=[app, msg])
    thr.start()

    return thr
