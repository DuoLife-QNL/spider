# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueTangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school = scrapy.Field()
    course_num = scrapy.Field()

class LianJiaItem(scrapy.Item):
    name = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    location3 = scrapy.Field()
    room_type = scrapy.Field()
    area = scrapy.Field()
    total_price = scrapy.Field()
    avg_price = scrapy.Field()