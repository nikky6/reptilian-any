# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from reptilian.items import JobboleArticItem
from tools.common import make_md5
from reptilian.items import CommonItemLoader
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider


class JobboleSpider(RedisSpider):
    name = 'jobbole'
    redis_key = 'jobbole:requests'
    allowed_domains = ['jobbole.com']
    # start_urls = ['http://blog.jobbole.com/all-posts/']

    def start_requests(self):
        yield Request('http://blog.jobbole.com/all-posts/')

    def parse(self, response):
        '''
        获取文章内容交给scrapy
        获取下一页url交给下载器
        :param response:
        :return:
        '''
        # 解析本一页
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        current_num = response.css(".page-numbers.current::text").extract_first()
        for post_node in post_nodes:
            post_url = post_node.css('a::attr(href)').extract()[0]
            try:
                image_url = post_node.css('img::attr(src)').extract()[0]
            except:
                image_url = ''

            yield Request(parse.urljoin(response.url, post_url),
                          meta={"current_num": current_num, "image_url": parse.urljoin(response.url, image_url)},
                          callback=self.parse_detail)

        # 提取下一页
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_urls:
            yield Request(next_urls, callback=self.parse)

    def parse_detail(self, response):

        item_loader = CommonItemLoader(item=JobboleArticItem(), response=response)

        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", make_md5(response.url))
        item_loader.add_value("image_url", response.meta['image_url'])

        item_loader.add_xpath("title",'//div[@class="entry-header"]/h1/text()')
        item_loader.add_xpath("create_date",'//p[@class="entry-meta-hide-on-mobile"]/text()')
        item_loader.add_xpath("love_num","//div[@class='post-adds']/span[contains(@class,'vote-post-up')]/h10/text()")
        item_loader.add_xpath("fav_num","//div[@class='post-adds']/span[contains(@class,'bookmark-btn')]/text()")

        item_loader.add_value("current_index", response.meta['current_num'])
        artic_item = item_loader.load_item()


        yield artic_item
