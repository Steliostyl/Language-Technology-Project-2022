import functions
import nltk_functions

articles = functions.readJSON('articles.json')
pos_tags, pos_tags_no_sw = nltk_functions.pos_tag(articles)
functions.saveListToJSON(pos_tags, 'pos_tags.json')
functions.saveListToJSON(pos_tags_no_sw, 'pos_tags_no_stopwords.json')

#for article in functions.readJSON('articles.json'):
#    print(article['id'], article['title'],'\n')