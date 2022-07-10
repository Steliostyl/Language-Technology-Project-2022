import functions
import nltk_functions

articles = functions.readJSON('websitescraper/cnbc_spider_new.json')
#print(type(articles[0].paragraphs[0]),articles[0].paragraphs[0])
for article in articles:
    #print(type(article.paragraphs), article.paragraphs)
    nltk_functions.pos_tag(article)
    #article.printArticle()