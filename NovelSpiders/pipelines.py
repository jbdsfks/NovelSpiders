# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utils.sql import Sql


class NovelspidersPipeline(object):
    def process_item(self, item, spider):
        # spider.logger.info(item)
        # print item
        sql = Sql()
        # print item
        sql.save_novel(item)
        return item