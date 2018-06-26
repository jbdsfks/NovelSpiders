# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    background = scrapy.Field()
    length = scrapy.Field()
    last_update = scrapy.Field()
    content = scrapy.Field()
    pass


class ChaptersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    novel_id = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    pass
