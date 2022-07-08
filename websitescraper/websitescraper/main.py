import functions
#import nltk_functions

articles = functions.readJSON('websitescraper/cnbc_spider_new.json')

for article in articles:
    article.printArticle()