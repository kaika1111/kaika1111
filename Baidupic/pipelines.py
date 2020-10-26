# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy .pipelines.images import ImagesPipeline
import scrapy
class BaidupicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item['url']
        yield scrapy.Request(url)



