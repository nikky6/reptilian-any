# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import random


class BigmeddataSpider(scrapy.Spider):
    name = 'bigmeddata'
    allowed_domains = ['bigmeddata.com']
    start_urls = ['http://bigmeddata.com/']

    def start_requests(self):
        yield Request('http://adminkf.bigmeddata.com/login')

    def parse(self, response):
        yield Request('http://adminkf.bigmeddata.com/login' + '?int=' + str(random.random()*100))
        print(response.url)