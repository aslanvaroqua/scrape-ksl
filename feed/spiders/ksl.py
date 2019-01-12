# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from ..inmate import Inmate
import csv, re

class Ksl(SitemapSpider):
    name = "ksl"
    sitemap_urls = ['https://classifieds.ksl.com/sitemap-subcategory.xml']
    sitemap_rules = [
        ('Baby', 'parse')
        ('Clothing', 'parse')

   ]
"""
    Baby
    Books and Media
    Clothing
    Computers
    Cycling
    Electronics
    Furniture
    General
    Industrial
    Musical
    Instruments
    Outdoors and Sporting
    Recreational
    Vehicles
    Services
    Toys
    Weddings
    Winter
    Sports


"""




    def parse(self,response):
        contact = Contact()


        yield contact
