# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):

    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com']

    rules = (
        Rule(LinkExtractor(allow='zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow='jobs/\d+.html'), callback='parse_job', follow=True),
    )

    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=ABAAABAAAIAACBIA6EBFE9CB392E94066F79AAFD02F11F8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541839216; _ga=GA1.2.473025921.1541839216; user_trace_token=20181110164231-8fc6fff0-e4c4-11e8-8812-5254005c3644; LGUID=20181110164231-8fc702f8-e4c4-11e8-8812-5254005c3644; _gid=GA1.2.961010956.1541839216; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=a296e9ef64b651b274d69416372223c2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166fcca6087143-0902f9f7feb0b-1e396652-1296000-166fcca60883c8%22%2C%22%24device_id%22%3A%22166fcca6087143-0902f9f7feb0b-1e396652-1296000-166fcca60883c8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _qddaz=QD.55fca9.pxhi6y.jobs9n7i; _gat=1; LGSID=20181111023108-ca684c29-e516-11e8-99af-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fhouduankaifaqita%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=a692afdc63b04c68af02662906ecd0e5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541874660; LGRID=20181111023314-158b2477-e517-11e8-8866-5254005c3644',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        }
    }

    def login(self):
        pass

    def parse_job(self, response):
        print(response.url)
