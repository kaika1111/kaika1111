# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LolItem1(scrapy.Item):
    win_postion = scrapy.Field()
    win_num = scrapy.Field()
    win_hero_name = scrapy.Field()
    win_Win_Rate = scrapy.Field()
    win_Pick_Rate = scrapy.Field()

class LolItem2(scrapy.Item):
    pick_postion = scrapy.Field()
    pick_num = scrapy.Field()
    pick_hero_name = scrapy.Field()
    pick_Win_Rate = scrapy.Field()
    pick_Pick_Rate = scrapy.Field()

class LolItem3(scrapy.Item):
    ban_postion = scrapy.Field()
    ban_num = scrapy.Field()
    ban_hero_name = scrapy.Field()
    ban_Ban_Rate = scrapy.Field()

