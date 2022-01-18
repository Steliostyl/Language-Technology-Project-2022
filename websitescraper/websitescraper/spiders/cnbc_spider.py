from cgitb import text
import scrapy

class CnbcSpider(scrapy.Spider):
    name = 'cnbc_spider'
    start_urls = ['https://www.cnbc.com/2022/01/18/covid-could-be-turning-kids-into-fussy-eaters-due-to-loss-of-smell.html']

    # response.xpath('//div[@class="d-intro-hed"]/p/span/text()').extract_first()

    def parse(self, response):
        #final_text = ''
        #tempAuthor = response.xpath('//a[@class="Author-authorName"]/text()').extract_first()
        #if tempAuthor is None:
        #    tempAuthor = response.xpath('//a[@class="Author-authorNameAndSocial"]//text()').extract_first()
        #    print("It's None")
        yield { 
            'article_title': response.xpath('//h1/text()').extract_first(),
            'article_tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            #'article_date': response.xpath('//time/text()').extract(),
                'author': response.xpath('//div[@class="Author-authorNameAndSocial"]//text()').extract_first(),
            'article_datetime': response.css('time::attr(datetime)').get(),
            'paragraph_headers': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]/h3/text()').extract(),
            'paragraphs': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]//text()').extract()
        }