# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class HwPipeline(object):

    def open_spider(self, spider):
        try: #打开 json 文件
            self.file = open('Data.csv', "a", encoding="utf 8")
        except Exception as err:
            print(err)
    def process_item (self, item, spider):
        # dict_item = dict(item) #生成字典对象
        # json_str = json.dumps(dict_item, ensure_ascii =False) + "\n" #生成json 串
        # self.file.write(json_str) #将 json 串写入到文件中
        self.file.write('"{}",'.format(item['name']))
        self.file.write('"{}",'.format(item['location1']))
        self.file.write('"{}",'.format(item['location2']))
        self.file.write('"{}",'.format(item['location3']))
        self.file.write('"{}",'.format(item['room_type']))
        self.file.write('"{}",'.format(item['area']))
        self.file.write('"{}",'.format(item['total_price']))
        self.file.write('"{}"\n'.format(item['avg_price']))
        return item
    def close_spider(self,spider):
        self.file.close() #关闭文件
