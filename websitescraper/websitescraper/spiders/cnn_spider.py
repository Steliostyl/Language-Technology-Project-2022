from cgitb import text
import scrapy

class CnnSpider(scrapy.Spider):
    name = 'cnn_spider'
    start_urls = ['https://edition.cnn.com/interactive/2022/01/world/greenland-denmark-social-experiment-cmd-idnty-intl-cnnphotos/']

    # response.xpath('//div[@class="d-intro-hed"]/p/span/text()').extract_first()

    def parse(self, response):
        #final_text = ''
        yield { 'article_title': response.xpath('//div[@class="d-intro-hed"]/h1/text()').extract() }
        yield { 'story_details': response.xpath('//div[@class="d-intro-hed"]/p/span/text()').extract() }

        for text_container in response.xpath('//div[@class="cp-text container"]/p'):
            note_title = text_container.xpath('strong/em')
            if note_title:
                yield {
                    'note_title': note_title.xpath('text()').extract(),
                    'note_text': text_container.xpath('em/text()').extract()
                }
            else:
                yield { 
                    'text': text_container.xpath('text()').extract()
                }