# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exceptions import DropItem


class MediumDotComJsonlOutput(object):
    def __init__(self, outputfile=create_filename()):
        self.files = {}
        self.outputfile = outputfile
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        print('jsonl output class activated')
        file = open('items.jl', 'w+b')
        self.files[spider] = file
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()
        
    def spider_closed(self, spider):
        print('jsonl output class dectivated')
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
        
    def process_item(self, item, spider):
        if item['link']:
            print('writing to jsonl')
            self.exporter.export_item(self, item)
            return item
        else:
            raise DropItem("No link data.")


