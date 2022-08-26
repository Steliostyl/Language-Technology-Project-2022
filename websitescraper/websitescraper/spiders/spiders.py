import scrapy
import re
from html_text import extract_text
from datetime import datetime


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
        paragraphs = ''
        for paragraph in par:
            paragraphs += ' ' + extract_text(paragraph)

        article = { 
            'id': self.article_id,
            'title': response.xpath('//h1/text()').extract_first(),
            'tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            'author': response.xpath('//div[@class="Author-authorNameAndSocial"]//text()').extract_first(),
            'datetime': readDateTimeFromString(response.css('time::attr(datetime)').get()),
            'paragraphs': paragraphs,
            'url': response.url
        }
        self.article_id += 1

        return article


class CnnSpider(scrapy.Spider):
    name = 'cnn_spider'
    start_urls = ['https://edition.cnn.com/']
    allowed_domains = ['cnn.com']
    article_id = 0

    def parse(self, response):
        categories = response.xpath('//footer//nav/ul[@type="expanded"]/li/a/@href')
        #print(categories)
        for category in categories:
            if category.get() == '/more' or category.get() == '/videos':
                continue
            print(category)
            print(category.get())
            yield response.follow(category.get(), callback=self.parse_category)
    
    def parse_category(self, response):
        containers = response.xpath('//div[starts-with(@class, "l-container")]')
        #print(len(containers))

        for container in containers:
            section = container.xpath('./div[@class="zn-header"]/h2[@class="zn-header__text"]/text()').extract_first()
            if section == None or "partner content" in section.lower():
                continue
            print(section)
            for link in container.xpath('//*[starts-with(@class, "column zn__column")]//@href'):
                #print('Article ID: ',self.article_id,' Article url: ', link, '') 
                self.article_id += 1
                yield response.follow(link.get(), callback=self.parse_article, meta={'section': section})


    def parse_article(self, response):
        article = { 
            'section': response.meta.get('section'),
            'title': response.xpath('//h1/text()').extract(),
            'url': response.url
        }

        invalid_titles = [ None, '']
        if article['title'] in invalid_titles:
            return

        #for key, value in article.items():
        #    print(key, value)
        return article