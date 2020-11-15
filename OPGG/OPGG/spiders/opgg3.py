import scrapy
from LOL.items import LolItem3
import re

class Opgg3Spider(scrapy.Spider):
    name = 'opgg3'
    allowed_domains = ['www.op.gg']
    start_urls = ['https://www.op.gg/champion/ajax/statistics/trendChampionList/type=banratio&']
    custom_settings = {
        'ITEM_PIPELINES': {
        'LOL.pipelines.LolPipeline3': 100,
        }
    }
    def parse(self, response):
        item = LolItem3()
        for n in range(1, 152):
            item['ban_num'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[1]/text()' % n).extract()[0]
            a = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[2]/text()' % n).extract()[0]
            item['ban_postion'] = re.findall('(Top|Jungle|Middle|Bottom|Support)', a)
            item['ban_hero_name'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[1]/text()' % n).extract()[0]
            item['ban_Ban_Rate'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[4]/text()' % n).extract()[0]
            yield item

