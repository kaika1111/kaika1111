import scrapy
import json
from Baidupic.items import BaidupicItem
class BaidupicSpider(scrapy.Spider):
    name = 'baidupic'
    base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexhot&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=pcindexhot&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn='
    offset = '30'
    start_urls = [base_url + offset]
    def parse(self, response):
        for m in range(31):
            n = json.loads(response.body)['data'][m]
            item = BaidupicItem()
            item['url'] = n['hoverURL']
            yield item
    # def download_pic(self):
