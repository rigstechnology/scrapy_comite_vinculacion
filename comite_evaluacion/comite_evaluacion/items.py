# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComiteEvaluacionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    company = scrapy.Field()
    position = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    pass
