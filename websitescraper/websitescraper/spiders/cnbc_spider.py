import scrapy
from scrapy.crawler import CrawlerProcess

class CnbcSpider(scrapy.Spider):
    name = 'cnbc_spider'
    start_urls = ['https://www.cnbc.com/world/?region=world']

    def parse(self, response):
        for link in response.xpath('//ul[@class="LatestNews-list"]//a[@class="LatestNews-headline"]/@href'):
            yield response.follow(link.get(), callback=self.parse_article)
    
    def parse_article(self, response):
        yield { 
            'article_title': response.xpath('//h1/text()').extract_first(),
            'article_tag': response.xpath('//a[@class="ArticleHeader-eyebrow"]/text()').extract_first(),
            'author': response.xpath('//div[@class="Author-authorNameAndSocial"]//text()').extract_first(),
            'article_datetime': response.css('time::attr(datetime)').get(),
            'paragraphs': response.xpath('//div[@class="ArticleBody-articleBody"]/div[@class="group"]/p').extract(),
            'url': response.url
        }


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(CnbcSpider)
    process.start() # the script will block here until the crawling is finished
