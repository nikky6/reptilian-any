# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import random

class SdifenSpider(RedisSpider):
    name = 'sdifen'
    redis_key =  'sdifen:start_urls'

    start_urls = [
        'http://blog.jobbole.com/all-posts/'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)

    def parse(self, response):
        print("1"*100)
