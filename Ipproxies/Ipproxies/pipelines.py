# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
class IpproxiesPipeline:
    # def __init__(self):
    #     self.f = open('Ipproxies.json','wb')
    # def process_item(self, item, spider):
    #     content = json.dumps(repr(dict(item)),ensure_ascii=False) +',\n'
    #     self.f.write(content)
    #     return item
    # def close_spide(self,spider):
    #     self.f.close()
    def process_item(self, item, spider):
        data = item
        data2 = json.dumps(str(data),ensure_ascii=False)
        with open('Ipproxies.txt','a',encoding='utf-8') as f:
            f.write(data2 + '\n')
        return item