import functions

articles = functions.readJSON('cnbc_spider.json')

for article in articles:
    article.printArticle()