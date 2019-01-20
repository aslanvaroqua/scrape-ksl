# ksl-scraper
Scraper of the KSL classifieds [classifieds.ksl.com](https://classifieds.ksl.com/), written in Python Scrapy.

## Basic usage
There are spiders for each category: 

i.e

1. `computers` scrapes all computers for sale 
2. `outdoors` scrapes all outdoors items.

There is also a single large scraper for all the categories at once. 

After installing [Scrapy](www.scrapy.org), in the project directory simply run the command

`scrapy crawl ksl`

or for specific category:

`scrapy crawl computers`

to generate a CSV file with the data 

to generate an `computers.csv` with data from computers cateogory 



## cloud

projects:
  default: 12345
  prod: 33333

requirements:
  file: requirements.txt

In case you use pipenv you may also specify a Pipfile:

### project_directory/scrapinghub.yml

projects:
   default: 12345 
   prod: 33333
requirements:
   file: Pipfile


## deploy


To deploy a Scrapy project to Scrapy Cloud, navigate into the project’s folder and run:

`
shub deploy [TARGET]
`

where [TARGET] is either a project name defined in scrapinghub.yml or a numerical Scrapinghub project ID. If you have configured a default target in your scrapinghub.yml, you can leave out the parameter completely:

`
$ shub deploy
Packing version 3af023e-master
Deploying to Scrapy Cloud project "12345"
{"status": "ok", "project": 12345, "version": "3af023e-master", "spiders": 1}
`

Run your spiders at: https://app.scrapinghub.com/p/12345/

## Proxy

you can set the proxy list in proxy.txt. If you don't they will block you. The ones provided work as of January 10, 2018. There are free proxy lists you can find online. 


## Fields
The scraped data contains the following fields (see contact.py):


`
class Contact(scrapy.Item):

    cell_phone = scrapy.Field()
    
    home_phone = scrapy.Field()
    
    category = scrapy.Field()
    
    sub_category = scrapy.Field()
    
    city = scrapy.Field()
    
    state = scrapy.Field()
   
    zip = scrapy.Field()
    
    member_id = scrapy.Field()
`

## MONGODB

To enable mongodb... set the settings and uncomment the lines in pipelines. 





### info

A project by Skyscrapy, a service of Skylines Digital USA [skylinesdigital.com](https://skylinesdigital.com/)

  <img center height="300px" width="auto" src="https://img1.wsimg.com/isteam/ip/d2ec0c86-31b9-4318-b5b7-8df5b0940e94/logo/e417473e-4d57-4cf7-ba9d-ff34d6859768.png" align="center" />

``
Aslan Varoqua
Skylines Digital USA 
Denver, Colorado USA

https://skylinesdigital.com
https://linkedin.com/in/skyceo
``


