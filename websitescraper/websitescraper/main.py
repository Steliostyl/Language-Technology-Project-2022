import functions
import nltk_functions

# Read JSON created by the crawler
articles = functions.readJSON('articles.json')
functions.readAndTagArticles(articles)

# PoS tag articles with and without stop words
pos_tags, temp = nltk_functions.pos_tag(articles)
pos_tags_no_sw  = temp[0]
articles_w_count = temp[1]
lemmas = temp[2]

# Save pos tags to seperate files
functions.saveListToJSON(pos_tags, 'pos_tags.json')
functions.saveListToJSON(pos_tags_no_sw, 'pos_tags_no_stopwords.json')
lemmas = functions.calculateTFidf(lemmas, articles_w_count)
functions.createXML(lemmas)
functions.readXML('lemmas.xml')

#first_dict_keys = list(lemmas.keys())[:10]
#for key in first_dict_keys:
#    print(key, '\n', lemmas[key])

# lemmas_in_articles = lemmatized pos_tags_no_sw
# lemmas = functions.createLemmaDict(lemmas_in_articles)
# functions.createXML(lemmas)

#for article in functions.readJSON('articles.json'):
#    print(article['id'], article['title'],'\n')