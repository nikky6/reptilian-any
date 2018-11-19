#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 1:08 AM
# @Author  : Nikky
# @Site    : 
# @File    : common.py
import hashlib, re, requests


def make_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def get_md():
    url = "https://www.aigupiao.com/Dynamic/others?m_u_id=296904"
    result = requests.get(url)
    try:
        md = re.findall('var _Libs={"md":"(.*?)"}', result.text, re.S)[0]
    except:
        pass
    return md or None


def send_msg(url,data):
    requests.post(
        url,
        json=data
    )


if __name__ == '__main__':
    print(get_md())
