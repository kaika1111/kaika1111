# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class LolPipeline1:
    def __init__(self):
        self.f = open("win_data.json",'wb')
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False).encode()
        self.f.write(data+b'\n')
        return item
    def close_item(self):
        self.f.close()

class LolPipeline2:
    def __init__(self):
        self.f = open("pick_data.json",'wb')
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False).encode()
        self.f.write(data+b'\n')
        return item
    def close_item(self):
        self.f.close()

class LolPipeline3:
    def __init__(self):
        self.f = open("ban_data.json",'wb')
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False).encode()
        self.f.write(data+b'\n')
        return item
    def close_item(self):
        self.f.close()

