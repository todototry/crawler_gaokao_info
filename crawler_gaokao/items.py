# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerGaokaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school_id = scrapy.Field()
    school_name = scrapy.Field()
    price = scrapy.Field()

    pici1 = scrapy.Field()
    count1 = scrapy.Field()

    pici2 = scrapy.Field()
    count2 = scrapy.Field()

    pici3 = scrapy.Field()
    count3 = scrapy.Field()

    pici4 = scrapy.Field()
    count4 = scrapy.Field()

    pici5 = scrapy.Field()
    count5 = scrapy.Field()

    pici6 = scrapy.Field()
    count6 = scrapy.Field()

    pici7 = scrapy.Field()
    count7 = scrapy.Field()

    pici8 = scrapy.Field()
    count8 = scrapy.Field()

