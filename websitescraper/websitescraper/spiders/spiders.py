import scrapy
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
    start_urls = ['https://edition.cnn.com/world/']
    article_id = 0

    def parse(self, response):
        #for link in response.xpath('//ul[@class="LatestNews-list"]//a[@class="LatestNews-headline"]/@href'):
        #for link in response.css('[class^="column zn__column"]//@href'):

        #print(response.xpath('//*[starts-with(@class, "l-container")]').getall())
        containers = response.xpath('//div[starts-with(@class, "l-container")]')
        print(len(containers))

        for container in containers:
            t = container.xpath('./div[@class="zn-header"]/h2[@class="zn-header__text"]/text()').extract_first()
            if t == None or "partner content" in t:
                continue
            print(t)
            for link in container.xpath('//*[starts-with(@class, "column zn__column")]//h3[@class="cd__headline"]/@href'):
                print('Article ID: ',self.article_id,' Article url: ', link, '') 
                self.article_id += 1
                yield response.follow(link.get(), callback=self.parse_article)
    
    def parse_article(self, response):
        article = { 
            'title': response.xpath('//h1/text()').extract_first(),
            'url': response.url
        }
        for key, value in article.items():
            print(key, value)
        return article