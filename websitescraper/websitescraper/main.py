from tracemalloc import start
import functions
import nltk_functions
from time import perf_counter

# Read JSON created by the crawler
articles = functions.readJSON('articles.json')

# PoS tag articles with and without stop words
pos_tags, temp = nltk_functions.pos_tag(articles)
pos_tags_no_sw  = temp[0]
articles_w_count = temp[1]
lemmas = temp[2]

# Save pos tags to seperate files
functions.saveListToJSON(pos_tags, 'pos_tags.json')
functions.saveListToJSON(pos_tags_no_sw, 'pos_tags_no_stopwords.json')

# Calculate TFidf and save them as weights to the lemma dictionary
lemmas = functions.calculateTFidf(lemmas, articles_w_count)
#print(lemmas)
functions.createXML(lemmas)

## Load lemmas from XML file to a dictionary
#lemmas_from_file = functions.readXML('lemmas.xml')
## Save the loaded lemmas to file to check that loading was succesful
#functions.createXML(lemmas_from_file)

# Make queries and benchmark 
# time required to find the article ids
query_words = [
    "prospective", "be","having","second","fell","estate","adjustment","value","recovery","owner","midst","press","wharton"
]
start_time = perf_counter()
query_response = {}
for query in query_words:
    query_response[query] = nltk_functions.nltk_query(lemmas, query)
finish_time = perf_counter()
e_time = finish_time - start_time
for item in query_response.items():
    print(item)
print("Elapsed time: %.6f" % e_time)


#first_dict_keys = list(lemmas.keys())[:10]
#for key in first_dict_keys:
#    print(key, '\n', lemmas[key])
#    print(article['id'], article['title'],'\n')