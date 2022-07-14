import json
import nltk_functions
from xml.dom import minidom

# Function to read the articles from the JSON file
def readJSON(filename):
    with open(filename, 'r') as file:
        articles = json.load(file)
    return articles

def saveListToJSON(input_list, filename):
    # Open the file with filename (if it exists, it gets 
    # overwritten because of the use of w instead of a)
    with open(filename, 'w') as file:
        file.write('[\n')
        for index, list_el in enumerate(input_list):
            json.dump(list_el, file, indent=4, default=str)
            if index < len(input_list) - 1:
                file.write(',\n')
        file.write('\n]')
    file.close()

def readAndTagArticles(articles):
    # PoS tag articles with and without stop words
    pos_tags, pos_tags_no_sw = nltk_functions.pos_tag(articles)
    # Save pos tags to seperate files
    saveListToJSON(pos_tags, 'pos_tags.json')
    saveListToJSON(pos_tags_no_sw, 'pos_tags_no_stopwords.json')

def createLemmaDict(lemmas_in_articles):
    lemmas = {}
    article_w_count = []
    #article_w_count[article_id] = word count of article with id = article_id

    # Calculate the appearance count for each word in each article
    # (later to be turned into tf)
    for article_id, article in enumerate(lemmas_in_articles):
        # This only works because article ids are 
        # identical with their order of appearance
        # in the article list and pos_tags
        article_w_count.append(len(lemmas_in_articles[article_id]))
        for sentence in article:
            for lemma in sentence:
                if lemma not in lemmas.keys():
                    lemmas['word'] = {
                        article_id: 1
                    }
                else:
                    lemmas['word'][article_id] += 1

    article_count = len(lemmas_in_articles)

    # Calculate weights for all words (using tf_idf)
    for lemma in lemmas:
        idf = len(lemmas[lemma].keys())/article_count
        for key in lemmas[lemma].keys():
            tf = lemmas[lemma][key]/article_w_count[key]
            lemmas[lemma][key] = tf*idf

    return lemmas

def calculateTFidf(lemmas, article_w_count):
    article_count = len(article_w_count)
    # Calculate weights for all words (using tf_idf)
    for lemma in lemmas:
        idf = len(lemmas[lemma].keys())/article_count
        for key in lemmas[lemma].keys():
            tf = lemmas[lemma][key]/article_w_count[key]
            lemmas[lemma][key] = tf*idf

    return lemmas


def createXML(lemmas_dict):
    #lemmas example
    #lemmas = {
    #    'pen':{
    #        '1': 0.1,
    #        '2': 0.2
    #    },
    #    'pineapple':{
    #        '1': 0.3,
    #        '2': 0.4
    #    }
    #}

    root = minidom.Document()
    inv_index = root.createElement('inverted_index')
    root.appendChild(inv_index)

    for word in lemmas_dict.keys():
        new_lemma = root.createElement('lemma')
        new_lemma.setAttribute('name', word)
        for key in lemmas_dict[word].keys():
            new_document = root.createElement('document')
            new_document.setAttribute('id', str(key))
            new_document.setAttribute('weight', str(lemmas_dict[word][key]))
            new_lemma.appendChild(new_document)
        inv_index.appendChild(new_lemma)

    xml_str = root.toprettyxml(indent ="\t")
    
    with open('lemmas.xml', "w") as f:
        f.write(xml_str) 