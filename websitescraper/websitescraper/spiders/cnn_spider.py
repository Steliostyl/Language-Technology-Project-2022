from cgitb import text
import scrapy

class CnnSpider(scrapy.Spider):
    name = 'cnn_spider'
    start_urls = ['https://www.cnbc.com/2022/01/15/how-the-us-fell-way-behind-in-lithium-white-gold-for-evs.html']

    # response.xpath('//div[@class="d-intro-hed"]/p/span/text()').extract_first()

    def parse(self, response):
        #final_text = ''
        yield { 
            'article_title': response.xpath('//h1/text()').extract_first(),
            'article_tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            #'article_date': response.xpath('//time/text()').extract(),
            'article_datetime': response.css('time::attr(datetime)').get(),
            'author': response.xpath('//a[@class="Author-authorName"]/text()').extract(),
            'paragraph_headers': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]/h3/text()').extract(),
            'paragraphs': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]//text()').extract()
        }