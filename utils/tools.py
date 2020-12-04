#!/usr/bin/env python
# encoding: utf-8
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379,encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)