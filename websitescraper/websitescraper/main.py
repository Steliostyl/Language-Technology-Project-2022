import functions
import nltk_functions

articles = functions.readScraperJSON('cnbc_spider_new.json')
functions.createNewJSONforProcessedArticles('processed_articles.json')


for article in articles:
    nltk_functions.pos_tag(article)
    
functions.saveArticlesToJSON(articles)
functions.cleanupJSONfile()