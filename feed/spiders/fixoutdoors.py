# -*- coding: utf-8 -*-
import scrapy
from ..contact import Contact
import csv
import json


class KSLFixIndSpider(scrapy.Spider):
    name = "fixout"
    category = [
        #"Baby",
        #"Books and Media" 
        #"Clothing and Apparel", 
        #"Computers",
        #"Cycling",
        #"Electronics",
        #"Furniture",
        #"General",
        #"Industrial",
        #"Musical Instruments",
        "Outdoors and Sporting",
        #"Recreational Vehicles",
        #"Tickets", #
        #"Toys",#
        #"Weddings",#
        #"Winter Sports"#
    ]

    resultfile = open('fixout.csv', mode='w', newline='')
    writer = csv.writer(resultfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def start_requests(self):
        header_row = ['name', 'member_id']
        self.writer.writerow(header_row)

        urls = []
        for cat in self.category:
            urls.append('https://classifieds.ksl.com/s/{}'.format(cat))

        # urls = [
        #     'https://classifieds.ksl.com/s/Baby'
        # ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ttt = response.xpath('//span[@class="total-listings"]').xpath("text()").extract_first()
        ttt = ttt.replace(',', '').strip()
        count = int(ttt)

        if count == 0:
            yield scrapy.Request(url=response.url, dont_filter=True)

        # url = 'https://classifieds.ksl.com/search/index?perPage=96'
        # yield scrapy.Request(url=url, callback=self.parse_page)

        for page in range(0, int(count/24)):
            url = 'https://classifieds.ksl.com/search/index?page={}'.format(page)
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        print(response.url)
        txt = response.text
        pos1 = txt.find('listings:')
        pos2 = txt.find('}],', pos1 + 1)

        if pos1 == -1 or pos2 == -1:
            yield scrapy.Request(url=response.url, dont_filter=True)

        jsontxt = txt[pos1 + len('listings:'):pos2 + 2]
        dddd = json.loads(jsontxt)
        for item in dddd:
            t_row = []
            contact = {}

            contact['member_id'] = ''
            if 'memberId' in item:
                contact['member_id'] = item['memberId']

            
            contact['name'] = ''
            if 'name' in item:
                contact['name'] = item['name']
            print(contact)

            t_row.append(contact['member_id'])
            t_row.append(contact['name'])            
            self.writer.writerow(t_row)

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


