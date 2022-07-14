import json
import nltk_functions
from xml.dom import minidom
import math
import xmltodict
import pprint

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

def calculateTFidf(lemmas, article_w_count):
    article_count = len(article_w_count)
    # Calculate weights for all words (using tf_idf)
    for lemma in lemmas:
        idf = math.log2(article_count/len(lemmas[lemma].keys()))
        for key in lemmas[lemma].keys():
            tf = lemmas[lemma][key]/article_w_count[key]
            lemmas[lemma][key] = tf*idf

    return lemmas

def createXML(lemmas_dict):
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
    
    with open('lemmas.xml', "w") as file:
        file.write(xml_str) 

def readXML(filename):
    with open(filename, "r") as file:
        xml_file = file.read()

    my_dict = xmltodict.parse(xml_file)
    #for item in my_dict['inverted_index']['lemma'][:2]:
    #    pprint.pprint(item, indent=2)
    return my_dict
    
#readXML('lemmas.xml')