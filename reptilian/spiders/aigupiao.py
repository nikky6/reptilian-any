# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import requests
import re, json, time, datetime
from reptilian.items import CommonItemLoader, AigupiaoItem
from scrapy_redis.spiders import RedisSpider
from reptilian.tools.common import make_md5,send_msg,get_md,remove_html
from reptilian.tools.cache import Cache

class AigupiaoSpider(RedisSpider):

    name = 'aigupiao'
    redis_key = "aigupiao:start_url"
    allowed_domains = ['aigupiao.com']
    msg_url = "https://oapi.dingtalk.com/robot/send?access_token=44ca2dd00dc04fd4f20f92eaed75aa3fd314c375b0db8602e3516d66463f00fb"
    msg_other = "https://oapi.dingtalk.com/robot/send?access_token=5ceb4e63232c03c449e0f9c3947eb4dced490f3181a7b0a473fe96d016fa0714"
    group_list = {
        # 居士
        "602": "中线波段",
        "681": "短线博弈",
        # 缠行
        "86": "缠门",
        # 天策
        "23": "赤宫",
        "206": "阳殿",
        # 刀锋
        "814": "激进组",
        "855": "稳健组",
        # 涅槃
        "24": "轨道埋伏",
        # 龙神
        "140": "默认分组",
        # 天龙八步组
        "584": "天龙八步组",
    }

    start_urls = [
        # "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=2&time={}",   # 刀锋投研
        # "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=48&time={}",  # 天策看市
        "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=84&time={}",  # 缠行者
        # "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=585&time={}", # 居士
        # "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=57&time={}",   # 涅槃重生
        # "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=567&time={}" #姚老哥
        "https://www.aigupiao.com/api/liver_msg.php?source=pc&act=liver_center&md={}&id=699&time={}",  # 龙神
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url.format(get_md(), str((int(round(time.time() * 1000))))), callback=self.single_info)

    def single_info(self, response):

        result = json.loads(response.text)
        if result.get("rslt", "") == "succ" and result.get("msg_list"):
            for item in result.get("msg_list"):
                if item.get("kind") == "vip" or item.get("kind") == "free":
                    oid = item.get("id")
                    url = "https://www.aigupiao.com/api/live.php?act=load_detail&oid={0}&source=pc&md={1}&time={2}".format(oid,get_md(),str((int(round(time.time() * 1000)))))
                    yield Request(url, method='POST', callback=self.single_detail)

    def single_detail(self, response):
        result = json.loads(response.text)

        if result.get("rslt", "") == "succ":
            aigupiao_loader = CommonItemLoader(item=AigupiaoItem(), response=response)

            aigupiao_loader.add_value("id", result["show_detail"][0]['id'])
            aigupiao_loader.add_value("title", result["show_detail"][0]['title'])
            aigupiao_loader.add_value("comment", result["show_detail"][0]['comment'])
            aigupiao_loader.add_value("create_time", result["show_detail"][0]['rec_time'])
            aigupiao_loader.add_value("group_name", self.group_list.get(result["show_detail"][0]['g_id'], ""))


            aigupiao = aigupiao_loader.load_item()
            key = make_md5(str(aigupiao))
            cache = Cache()
            if not cache.get(key):
                cache.set(key,str(aigupiao),604800)
                data = {"msgtype": "text", "text": {
                    "content": "{}\r{}\r{}\r{}\r{}".format(aigupiao.get("create_time", ""), aigupiao.get("title", ""),
                                                       aigupiao.get("group_name", ""),remove_html(result["show_detail"][0]['biaoti']), aigupiao.get("comment", ""))}}

                if result["show_detail"][0]['g_id'] == 140:
                    send_msg(self.msg_url, data)
                else:
                    send_msg(self.msg_other,data)
            yield aigupiao






if __name__ == '__main__':
    aigupiao = AigupiaoSpider()
    print(aigupiao.send_msg())
