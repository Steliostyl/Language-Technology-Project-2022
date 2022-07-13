import scrapy
from html_text import extract_text
from datetime import datetime=

def readDateTimeFromString(datetimeString):
    return datetime.fromisoformat(datetimeString[:-2] + ":" + datetimeString[len(datetimeString)-2:])

class CnbcSpider(scrapy.Spider):
    name = 'cnbc_spider'
    start_urls = ['https://www.cnbc.com/world/?region=world']
    article_id = 0

    def parse(self, response):
        for link in response.xpath('//ul[@class="LatestNews-list"]//a[@class="LatestNews-headline"]/@href'):
            yield response.follow(link.get(), callback=self.parse_article)
    
    def parse_article(self, response):
        par = response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]/p').extract()
        if par == []:
            return
        self.article_id += 1
        paragraphs = ''
        for paragraph in par:
            paragraphs += ' ' + extract_text(paragraph)

        article = { 
            'id': self.article_id,
            'article_title': response.xpath('//h1/text()').extract_first(),
            'article_tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            'author': response.xpath('//div[@class="Author-authorNameAndSocial"]//text()').extract_first(),
            'article_datetime': readDateTimeFromString(response.css('time::attr(datetime)').get()),
            'paragraphs': paragraphs,
            'url': response.url
        }
        return article