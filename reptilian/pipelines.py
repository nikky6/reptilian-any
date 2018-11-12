# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import pymysql
import pymysql.cursors

class PricePipeline(object):

    def process_item(self, item, spider):
        pass


class JobboleArticPipeline(object):

    def process_item(self, item, spider):
        return item


class JobboleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if 'image_url' in item:
            for ok, val in results:
                try:
                    image_file_path = val['path']
                except:
                    image_file_path = ""
            item['image_file_path'] = image_file_path
        return item


class JobboleMysqlPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', 'zngz123456', 'reptilian', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into article(
            url,
            url_object_id,
            title,
            love_num,
            fav_num,
            current_index,
            image_url,
            create_date,
            image_file_path) values
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql, (
            item['url'],
            item['url_object_id'],
            item['title'],
            item['love_num'],
            item['fav_num'],
            item['current_index'],
            item['image_url'][0],
            item['create_date'],
            item.get('image_file_path', '')
        ))
        self.conn.commit()

    def close_spider(self):
        self.cursor.close()


from twisted.enterprise import adbapi


class MysqlTwistedPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        settings_dbparam = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            db=settings['MYSQL_DBNAME'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **settings_dbparam)

        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        pass

    def do_insert(self, cursor, item):
        insert_sql = "insert into article(url,url_object_id,title,love_num,fav_num,current_index,image_url,create_date,image_file_path) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_sql, (
            item['url'],
            item['url_object_id'],
            item['title'],
            item['love_num'],
            item['fav_num'],
            item['current_index'],
            item['image_url'][0],
            item['create_date'],
            item.get('image_file_path', '')
        ))


if __name__ == '__main__':
    print(1)
