# to run 
# scrapy crawl imdb_spider -o movies.csv

from urllib.parse import urljoin
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

class ImdbSpider(Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt9335498/']

    def parse(self, response):
        yield Request('https://www.imdb.com/title/tt9335498/fullcredits', callback = self.parse)
        

    def parse_full_credits(self, response):
        links = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        for link in links:
            yield Request('https://www.imdb.com/title/tt9335498/fullcredits', callback = self.parse_full_credits)


    def parse_actor_page(self, response):
        # element.css("::attr(id)")
        # element.css("div.filmo-row")
        # element.css("a::text")
        pass

