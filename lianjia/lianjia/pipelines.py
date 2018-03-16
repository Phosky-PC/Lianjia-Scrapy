# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    def __init__(self):
        self.mongo_uri = settings.get("MONGO_URI")
        self.mongo_db = settings.get("MONGO_DB")
        self.mongo_port = settings.get("MONGO_PORT")
        self.mongo_collection = settings.get("MONGO_COLLECTION")

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_uri, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        try:
            if self.db[self.mongo_collection].insert(dict(item)):
                print('保存成功')
                return True
            else:
                print('保存失败')
                return False
        except Exception:
            print('数据已存在')
            pass
        return item

    def close_spider(self, spider):
        self.client.close()
