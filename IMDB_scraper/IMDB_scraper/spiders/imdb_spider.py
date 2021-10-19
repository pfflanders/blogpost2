# to run 
# scrapy crawl imdb_spider -o movies.csv

from urllib.parse import urljoin
from scrapy.spiders import Spider
from scrapy.http import Request

class ImdbSpider(Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt9335498/']

    def start_requests(self):
        try: 
            if self.url: # if a url is passed with the -a argument then we use that
                yield Request(self.url)
        except:
            for url in self.start_urls:
                yield Request(url)
    
    def parse(self, response):
        yield Request(urljoin(response.url, 'fullcredits'), 
                      callback = self.parse_full_credits)
         

    def parse_full_credits(self, response):
        # collect list of actor links
        actor_links = [a.attrib["href"] for a in response.css("td.primary_photo a")]

        # iterate over links and yielding requests to our next function
        for link in actor_links:
            yield Request(urljoin(response.url, link), 
                          callback = self.parse_actor_page)

    def parse_actor_page(self, response):
        # get actor name
        name = response.css('div.name-overview span::text').get()
        
        # get list of movies
        movie_list = [item.css('a::text').get() for item in response.css('div.filmo-row')]

        # yield dict with actor & movie 
        for movie in movie_list:
            yield {
                "actor": name,
                "movie_or_TV_name": movie
            }
