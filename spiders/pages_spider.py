# encoding -*-utf-8-*-
"""
Spider to crawl medium.com story titles
"""
import scrapy
from scrapy.crawler import CrawlerProcess


class StorySpider(scrapy.Spider):
    name = 'mediumDotCom'
    start_urls = ["https://medium.com/"]
        
    def parse(self, response):
        self.log(' '.join(["URLs visited:", response.url]))
        stories = response.css("div.u-flex0")
        for story in stories:
            data = {
                'title': story.css("a::attr('aria-label')").extract(),
                'link': story.css("a::attr('href')").extract(),
                }
            yield data


if __name__ == '__main__':
    # Running the spider from within .py script
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
    process.crawl(StorySpider)
    process.start()

"""
$ scrapy runspider ./Intrepid-Interlopers/mediumDotCom/pages_spider.py - o .Intrepid-Interlopers/mediumDotCom/pages_spider.json

Output subset obtained-
$ more .Intrepid-Interlopers/mediumDotCom/pages_spider.json
.
.
.
{"title": ["A hacker stole $31M of Ether \u2014 how it happened, and what it means for Ethereum"], "link": ["https://medium.freecodecamp.org/a-hacker-stole-31m-of-ether-how-it-happened-and-what-it-means-for-ethereum-9e5dc29e33ce?source=reading_list---8------3-----------"]},
{"title": [], "link": ["https://medium.freecodecamp.org/a-hacker-stole-31m-of-ether-how-it-happened-and-what-it-means-for-ethereum-9e5dc29e33ce?source=reading_list---8------3-----------"]},
{"title": [], "link": ["https://medium.com/@hosseeb", "https://medium.freecodecamp.org/@hosseeb"]},
{"title": [], "link": ["https://medium.com/@hosseeb"]},
{"title": [], "link": []},
{"title": ["The Chicago Negro and the Warsaw Ghetto"], "link": ["https://medium.com/beotiscreative/the-chicago-negro-and-the-warsaw-ghetto-2413bbea84ea?source=reading_list---8------0-----------"]},
{"title": [], "link": ["https://medium.com/beotiscreative/the-chicago-negro-and-the-warsaw-ghetto-2413bbea84ea?source=reading_list---8------0-----------", "https://medium.com/beotiscreative/the-chicago-negro-and-the-warsaw-ghetto-2413bbea84ea?source=reading_list---8------0-----------"]},
{"title": [], "link": ["https://medium.com/@eveewing", "https://medium.com/@eveewing"]},
{"title": [], "link": ["https://medium.com/@eveewing"]},
{"title": [], "link": []},
{"title": [], "link": []},
.
.
.
"""
