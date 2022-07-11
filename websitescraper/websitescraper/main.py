import functions
import nltk_functions
import os

articles = functions.readScraperJSON('websitescraper/cnbc_spider_new.json')
functions.createNewJSONforProcessedArticles('processed_articles.json')


for article in articles:
    nltk_functions.pos_tag(article)
    #article.printArticle()

with open('processed_articles.json', 'rb+') as file:
    file.seek(-1, os.SEEK_END)
    file.truncate()

with open('processed_articles.json', 'a') as file:
    file.write('\n]\n}')

#print(type(articles[0].pos_tags))
#print(articles[0].paragraphs)
#print(articles[0].pos_tags)
