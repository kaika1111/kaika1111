import scrapy
from LOL.items import LolItem2
import re

class Opgg2Spider(scrapy.Spider):
    name = 'opgg2'
    allowed_domains = ['www.op.gg']
    start_urls = ['https://www.op.gg/champion/ajax/statistics/trendChampionList/type=pickratio&']
    custom_settings = {
        'ITEM_PIPELINES': {
        'LOL.pipelines.LolPipeline2': 200,
        }
    }
    def parse(self, response):
        item = LolItem2()
        for n in range(1,152):
            item['pick_num'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[1]/text()'%n).extract()[0]
            a = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[2]/text()'%n).extract()[0]
            item['pick_postion'] = re.findall('(Top|Jungle|Middle|Bottom|Support)',a)
            item['pick_hero_name'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[1]/text()'%n).extract()[0]
            item['pick_Win_Rate'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[5]/text()'%n).extract()[0]
            item['pick_Pick_Rate'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[4]/text()'%n).extract()[0]
            yield item
