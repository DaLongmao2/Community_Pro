#!/usr/bin/env python
# encoding: utf-8
from flask import jsonify


class HttpCode(object):
    Ok = 200
    ParamerError = 400


def RestfulResult(code, message="", data=None):
    return jsonify({'code': code, 'message': message, 'data': data})


def success(message="", data=None):
    return RestfulResult(HttpCode.Ok, message=message, data=data)


def params_error(message="", data=None):
    return RestfulResult(HttpCode.ParamerError, message=message, data=data)
