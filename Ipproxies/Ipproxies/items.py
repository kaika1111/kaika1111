# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IpproxiesItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    level = scrapy.Field()
    type = scrapy.Field()