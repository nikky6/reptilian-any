#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 下午6:26
# @Author  : Nikky
# @Site    :
# @File    : cache.py
from reptilian.settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PWD
import redis


class Cache:

    def __init__(self):
        self._db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PWD)

    def set(self, name, value, time=None):
        '''
        设置缓存
        :param name: key
        :param value: value
        :param time: 秒
        :return:
        '''
        self._db.set(name, value, time)

    def get(self, name):
        '''
        获取缓存
        :param name: key
        :return:
        '''
        return self._db.get(name)

    def delete(self, name):
        '''
        删除缓存
        :param name:
        :return:
        '''
        return self._db.delete(name)


if __name__ == '__main__':
    token = "3dd5194debe299f23e09e1a1c0bc101f"
    cache = Cache()
    cache.set('token:%s' % token, "18668129923", 3600 * 24 * 30)

    print(cache.get('token:%s' % token))
