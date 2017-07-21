# encoding -*-utf8-*-
"""
Spider to crawl medium.com story titles
"""
import scrapy

from pprint import pprint


class StoryTitlesSpider(scrapy.Spider):
    name = 'storyTitles'
    start_urls = ["https://medium.com/"]
    def __init__(self):
        self.parse(self.response)
        
    def parse(self, response):
        self.log(' '.join(["URLs visited:", response.url]))
        yield response
        
        
medium_spider = StoryTitlesSpider()
# resp = medium_spider.parse("https://medium.com/")


pprint(medium_spider.text)

