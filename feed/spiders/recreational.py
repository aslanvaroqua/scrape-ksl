# -*- coding: utf-8 -*-
import scrapy
from ..contact import Contact
import csv
import json


class KSLRecreationalSpider(scrapy.Spider):
    name = "ksl-recreational"
    category = [
        # "Baby",#
        #"Books and Media" #
        # "Clothing and Apparel", #
        # "Computers",#
        # "Cycling",#
        # "Electronics",#
        #"Furniture",
        #"General",#
        #"Industrial",#
        # "Musical Instruments",#
        # "Outdoors and Sporting",#
        "Recreational Vehicles",#
        # "Tickets", #
        # "Toys",#
        # "Weddings",#
        # "Winter Sports"#
    ]

    resultfile = open('outdoors.py.csv', mode='w', newline='')
    writer = csv.writer(resultfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def start_requests(self):
        header_row = ['name', 'home_phone', 'cell_phone', 'category', 'sub_category', 'city', 'state', 'zip']
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

            contact['cell_phone'] = ''
            if 'cellPhone' in item:
                contact['cell_phone'] = item['cellPhone']

            contact['home_phone'] = ''
            if 'homePhone' in item:
                contact['home_phone'] = item['homePhone']

            # if contact['cellPhone'] == '999-999-9999' or contact['homePhone'] == '999-999-9999':
            #     continue
            # if contact['cellPhone'] == '' and contact['homePhone'] == '':
            #     continue

            contact['category'] = ''
            if 'category' in item:
                contact['category'] = item['category']

            contact['sub_category'] = ''
            if 'subCategory' in item:
                contact['sub_category'] = item['subCategory']

            contact['city'] = ''
            if 'city' in item:
                contact['city'] = item['city']

            contact['state'] = ''
            if 'state' in item:
                contact['state'] = item['state']

            contact['member_id'] = ''
            if 'name' in item:
                contact['member_id'] = item['name']

            contact['zip'] = ''
            if 'zip' in item:
                contact['zip'] = item['zip']

            print(contact)

            t_row.append(contact['member_id'])
            t_row.append(contact['home_phone'])
            t_row.append(contact['cell_phone'])
            t_row.append(contact['category'])
            t_row.append(contact['sub_category'])
            t_row.append(contact['city'])
            t_row.append(contact['state'])
            t_row.append(contact['zip'])
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

