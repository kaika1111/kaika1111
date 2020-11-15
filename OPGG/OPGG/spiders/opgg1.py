import scrapy
import re
from LOL.items import LolItem1

class LolSpider(scrapy.Spider):
    name = 'opgg1'
    allowed_domains = ['www.op.gg']
    start_urls = ['https://www.op.gg/champion/ajax/statistics/trendChampionList/type=winratio&']
    custom_settings = {
        'ITEM_PIPELINES' : {
        'LOL.pipelines.LolPipeline1': 300,
        }
    }
    def parse(self, response):
        item = LolItem1()
        for n in range(1,152):
            item['win_num'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[1]/text()'%n).extract()[0]
            a = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[2]/text()'%n).extract()[0]
            item['win_postion'] = re.findall('(Top|Jungle|Middle|Bottom|Support)',a)
            item['win_hero_name'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[3]/a/div[1]/text()'%n).extract()[0]
            item['win_Win_Rate'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[4]/text()'%n).extract()[0]
            item['win_Pick_Rate'] = response.xpath('/html/body/div/table/tbody[1]/tr[%d]/td[5]/text()'%n).extract()[0]
        # item['change'] = response.xpath('').extract()
            yield item


