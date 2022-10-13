import scrapy


class BookscrapSpider(scrapy.Spider):
    name = 'bookscrap'
    allowed_domains = ['http://books.toscrape.com']
    start_urls = ['http://http://books.toscrape.com/']

    def parse(self, response):
        pass
