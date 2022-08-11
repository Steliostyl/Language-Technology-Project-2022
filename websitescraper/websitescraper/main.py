import functions
import nltk_functions
import random
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
functions.createXML(lemmas)


#query_words = [
#    "randomnonexistingword", "prospective buyer", "be","having","second","fell","estate","adjustment","value","recovery","owner","midst","press","wharton"
#]

# Create queries
lemmaKeys = list(lemmas.keys())
# 20 1-word queries
query_words = random.sample(lemmaKeys, 20)
# 20 2-word queries
for i in range(0,20):
    query_words.append(' '.join(random.sample(lemmaKeys, 2)))
# 30-triple word queries
for i in range(0,30):
    query_words.append(' '.join(random.sample(lemmaKeys, 3)))
# 30-quad word queries
for i in range(0,30):
    query_words.append(' '.join(random.sample(lemmaKeys, 4)))

#print(query_words[:2], query_words[20:22], query_words[40:42], query_words[70:72])

# Make queries and benchmark 
# time required to find the article ids
start_time = perf_counter()
query_response = {}
for query in query_words:
    query_response[query] = nltk_functions.nltk_query(lemmas, query)
finish_time = perf_counter()
e_time = finish_time - start_time
for item in query_response.items():
    print(item)
print("Elapsed time: %.6f" % e_time)