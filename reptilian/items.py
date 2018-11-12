# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime
import re


class ReptilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Identity


def modifyData(value):
    try:
        date = value.strip().replace('·', '').strip()
        create_date = datetime.strptime(date, '%Y/%m/%d')
    except:
        create_date = datetime.now().strftime('%Y/%m/%d')
    return create_date


def getNumber(value):
    if value:
        try:
            result = re.match('.*?(\d).*?', value.strip())
            return int(result.group(1))
        except:
            return 0
    return 0

def trimHtmlTags(value):
    if value:
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', value)
        return dd

class CommonItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobboleArticItem(scrapy.Item):
    url = scrapy.Field(
    )
    url_object_id = scrapy.Field(

    )
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(modifyData)
    )
    love_num = scrapy.Field(
        input_processor=MapCompose(getNumber)
    )
    fav_num = scrapy.Field(
        input_processor=MapCompose(getNumber)
    )
    current_index = scrapy.Field(

    )
    image_url = scrapy.Field(
        output_processor=Identity()
    )
    image_file_path = scrapy.Field(

    )


class AigupiaoItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    group_name = scrapy.Field()
    comment = scrapy.Field(
        input_processor=MapCompose(trimHtmlTags)
    )
    create_time = scrapy.Field()
