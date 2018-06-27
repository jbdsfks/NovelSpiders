# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utils.sql import Sql
from items import NovelsItem, ChaptersItem


class NovelspidersPipeline(object):
    def process_item(self, item, spider):
        sql = Sql()
        if isinstance(item, NovelsItem):
            sql.save_novel(item, spider)
        elif isinstance(item, ChaptersItem):
            sql.save_chapter(item, spider)
        return item
