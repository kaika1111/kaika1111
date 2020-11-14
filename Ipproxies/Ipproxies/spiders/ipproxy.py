import scrapy
import time
from Ipproxies.items import IpproxiesItem

class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    url = 'https://www.kuaidaili.com/free/inha/'
    offset = 1
    start_urls = [url+str(offset)]
    def parse(self, response):
        for n in range(1,16):
            item = IpproxiesItem()
            item['ip'] = response.xpath('.//tr[%d]/td[1]/text()'%n).extract()[0]
            item['port'] = response.xpath('.//tr[%d]/td[2]/text()'%n).extract()[0]
            item['level'] = response.xpath('.//tr[%d]/td[3]/text()'%n).extract()[0]
            item['type'] = response.xpath('.//tr[%d]/td[4]/text()'%n).extract()[0]
            yield item
        time.sleep(1)
        if self.offset<200:
            self.offset += 1
            new_url = self.url + str(self.offset)
            yield scrapy.Request(new_url,callback= self.parse)
