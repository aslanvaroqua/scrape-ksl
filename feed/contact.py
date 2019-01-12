# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Contact(scrapy.Item):
    cell_phone = scrapy.Field()
    home_phone = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()


    cell_phone,home_phone,category,sub_category = scrapy.Field()

