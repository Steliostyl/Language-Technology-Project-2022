from cgitb import text
import scrapy

class CnnSpider(scrapy.Spider):
    name = 'cnn_spider'
    start_urls = ['https://www.cnbc.com/2022/01/17/credit-suisse-needs-to-salvage-reputation-and-personnel-after-latest-scandal.html']

    # response.xpath('//div[@class="d-intro-hed"]/p/span/text()').extract_first()

    def parse(self, response):
        #final_text = ''
        yield { 
            'article_title': response.xpath('//h1/text()').extract_first(),
            'article_tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            'article_date': response.xpath('//time/text()').extract(),
            'author': response.xpath('//a[@class="Author-authorName"]/text()').extract(),
            'paragraphs': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]//text()').extract()
        }