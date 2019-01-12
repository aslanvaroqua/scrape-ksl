# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from ..contact import Contact
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import csv


class Ksl(SitemapSpider):
    name = "ksl"
    # allowed_domains = ["classifieds.ksl.com"]
    sitemap_urls = ['https://classifieds.ksl.com/sitemap-category.xml']

    sitemap_rules = [
("Baby","parse"),
("Media","parse"),
("Clothing","parse"),
("Computers","parse"),
("Cycling","parse"),
("Electronics","parse"),
("Furniture","parse"),
("General","parse"),
("Industrial","parse"),
("Musical","parse"),
("Instruments","parse"),
("Outdoors and Sporting","parse"),
("Recreational","parse"),
("Vehicles","parse"),
("Services","parse"),
("Toys","parse"),
("Weddings","parse"),
("Winter","parse"),
("Sports","parse"),]

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--lang=en")

    chrome_path = 'chromedriver'
    chrome = webdriver.Chrome(chrome_path, options=options)
    cnt = 0

    resultfile = open('ksl.csv', mode='w', newline='')
    writer = csv.writer(resultfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def parse(self, response):
        self.cnt += 1
        if self.cnt >= 2:
            return
        url = response.url
        self.chrome.get(url)
        self.chrome.implicitly_wait(2)
        # soup = BeautifulSoup(self.chrome.page_source, 'html.parser')
        txt = self.chrome.page_source
        pos1 = txt.find('listings:')
        pos2 = txt.find('}],', pos1+1)
        jsontxt = txt[pos1+len('listings:'):pos2+2]
        #print(jsontxt)
        dddd = json.loads(jsontxt)
        for item in dddd:
            t_row = []
            contact = Contact()
            contact['cell_phone'] = ''
            if 'cellPhone' in item:
                contact['cell_phone'] = item['cellPhone']

            contact['home_phone'] = ''
            if 'homePhone' in item:
                contact['home_phone'] = item['homePhone']

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
            if 'memberId' in item:
                contact['member_id'] = item['memberId']

            contact['zip'] = ''
            if 'zip' in item:
                contact['zip'] = item['zip']

            t_row.append(contact['member_id'])
            t_row.append(contact['home_phone'])
            t_row.append(contact['cell_phone'])
            t_row.append(contact['category'])
            t_row.append(contact['sub_category'])
            t_row.append(contact['city'])
            t_row.append(contact['state'])
            t_row.append(contact['zip'])
            self.writer.writerow(t_row)

            yield contact
        print('----------finished-{}-------------'.format(self.cnt))

