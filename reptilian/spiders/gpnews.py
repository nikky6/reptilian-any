#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 5:36 PM
# @Author  : Nikky
# @Site    : 
# @File    : gpnews.py
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
import time, json
from reptilian.tools.common import get_md, make_md5, send_msg
from reptilian.tools.cache import Cache


class GpnewsSpider(RedisSpider):
    name = 'gpnews'
    redis_key = "aigupiao:start_url"
    allowed_domains = ['aigupiao.com']
    msg_url = "https://oapi.dingtalk.com/robot/send?access_token=5ceb4e63232c03c449e0f9c3947eb4dced490f3181a7b0a473fe96d016fa0714"

    start_urls = [
        "https://www.aigupiao.com/index.php?s=/Api/Express/express_list&u_id=277218&md={}&time={}",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url.format(get_md(), str((int(round(time.time() * 1000))))), callback=self.single_parse)

    def single_parse(self, response):
        result = json.loads(response.text)
        if result.get("rslt", "") == "succ" and result.get("datalist"):
            for item_list in result.get("datalist"):
                for item in result.get("datalist").get(item_list).get('data'):
                    if item.get("important") == "yes":
                        id = item.get("id")
                        key = make_md5(str(id))
                        cache = Cache()
                        if not cache.get(key):
                            cache.set(key,str(id),604800)
                            data = {"msgtype": "text", "text": {
                                "content": "{}\r{}".format(item.get("rec_time_desc", ""), item.get("web_content", ""))}}
                            send_msg(self.msg_url,data)
                            yield data
        pass