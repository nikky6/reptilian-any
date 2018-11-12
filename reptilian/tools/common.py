#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 1:08 AM
# @Author  : Nikky
# @Site    : 
# @File    : common.py
import hashlib


def make_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    print(make_md5("demo"))