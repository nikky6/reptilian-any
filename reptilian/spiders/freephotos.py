# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FreephotosSpider(CrawlSpider):
    name = 'freephotos'
    allowed_domains = ['freephotos.cc']
    start_urls = ['http://freephotos.cc/']


    rules = (
        Rule(LinkExtractor(allow='zh/\w'), follow=True),
        Rule(LinkExtractor(allow='zh/\w#\d'), follow=True),
        Rule(LinkExtractor(allow='jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
