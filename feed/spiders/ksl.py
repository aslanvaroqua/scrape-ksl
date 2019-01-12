# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from ..contact import Contact
import csv, re

class Ksl(SitemapSpider):
    name = "ksl"
    sitemap_urls = ['https://classifieds.ksl.com/sitemap-subcategory.xml']
    sitemap_rules = [
        ('Baby', 'parse')
        ('Clothing', 'parse')

    ]
    
    def parse(self,response):
        contact = Contact()


        yield contact
