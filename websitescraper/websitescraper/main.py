import functions
import nltk_functions

articles = functions.readJSON('websitescraper/cnbc_spider_new.json')
functions.deleteFile('processed_articles.json')

for article in articles:
    nltk_functions.pos_tag(article)
    #article.printArticle()

#print(type(articles[0].pos_tags))
#print(articles[0].paragraphs)
#print(articles[0].pos_tags)
