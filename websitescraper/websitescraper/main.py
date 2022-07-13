import functions
import nltk_functions

articles = functions.readScraperJSON('cnbc_spider_new.json')


for article in articles:
    nltk_functions.pos_tag(article)
    
functions.createNewJSON('processed_articles.json')
functions.saveArticlesToJSON(articles, 'processed_articles.json')
functions.cleanupJSONfile('processed_articles.json')

articles_from_JSON = functions.readArticlesFromJSON('processed_articles.json')
nltk_functions.filter_stop_words_2(articles_from_JSON)

functions.createNewJSON('no_stop_words.json')
functions.saveArticlesToJSON(articles_from_JSON, 'no_stop_words.json')
functions.cleanupJSONfile('no_stop_words.json')
#print(articles_from_JSON[0]['pos_tags_no_stopwords'])