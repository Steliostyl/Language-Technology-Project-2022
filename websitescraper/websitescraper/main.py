import functions
import nltk_functions

# Read JSON created by the crawler
articles = functions.readJSON('articles.json')
functions.readAndTagArticles(articles)

# PoS tag articles with and without stop words
pos_tags, pos_tags_no_sw = nltk_functions.pos_tag(articles)

# Save pos tags to seperate files
functions.saveListToJSON(pos_tags, 'pos_tags.json')
functions.saveListToJSON(pos_tags_no_sw, 'pos_tags_no_stopwords.json')

# lemmas_in_articles = lemmatized pos_tags_no_sw
# lemmas = functions.createLemmaDict(lemmas_in_articles)
# functions.createXML(lemmas)

#for article in functions.readJSON('articles.json'):
#    print(article['id'], article['title'],'\n')