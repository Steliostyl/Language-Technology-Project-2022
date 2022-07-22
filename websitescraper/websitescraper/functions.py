from audioop import avg
import json
from xml.dom import minidom
import math
import xml.etree.ElementTree as ET

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

# Calculate weights for all lemmas (using tf_idf)
def calculateTFidf(lemmas, article_w_count):
    article_count = len(article_w_count)
    for lemma in lemmas:
        idf = math.log2(article_count/len(lemmas[lemma].keys()))
        lemmas[lemma]['total_weight'] = 0
        for key in lemmas[lemma].keys():
            if key == 'total_weight':
                continue
            tf = lemmas[lemma][key]/article_w_count[key]
            tf_idf = tf*idf
            lemmas[lemma][key] = tf_idf
            lemmas[lemma]['total_weight'] += tf_idf
        
        # Sort lemma documents by weight
        sorted_dict = {}
        sorted_keys = sorted(lemmas[lemma], key=lemmas[lemma].get, reverse=True)
        for key in sorted_keys:
            sorted_dict[key] = lemmas[lemma][key]
        
        # Replace dictionary with the sorted dictionary
        lemmas[lemma] = sorted_dict          

    return lemmas

def createXML(lemmas_dict):
    root = minidom.Document()
    inv_index = root.createElement('inverted_index')
    root.appendChild(inv_index)

    for word in lemmas_dict.keys():
        new_lemma = root.createElement('lemma')
        total_weight = str(lemmas_dict[word]['total_weight'])
        new_lemma.setAttribute('name', word)
        new_lemma.setAttribute('total_weight', total_weight)
        for key in lemmas_dict[word].keys():
            if key == 'total_weight':
                continue
            new_document = root.createElement('document')
            new_document.setAttribute('id', str(key))
            new_document.setAttribute('weight', str(lemmas_dict[word][key]))
            new_lemma.appendChild(new_document)
        inv_index.appendChild(new_lemma)

    xml_str = root.toprettyxml(indent ='\t')
    
    with open('lemmas.xml', "w") as file:
        file.write(xml_str) 

def readXML(filename):
    lemma_dict = {}
    root_node = ET.parse(filename).getroot()
    # Get all lemmas
    for lemma in root_node.findall('lemma'):
        lemma_name = lemma.get('name')
        docs = {}
        for document in lemma.findall('document'):
            id = document.get('id')
            weight = document.get('weight')
            docs[id] = weight
        
        lemma_dict[lemma_name] = docs
        lemma_dict[lemma_name]['total_weight'] = lemma.get('total_weight')
        
    return lemma_dict

def query(lemmas, word):
    articles = []
    for article_id in lemmas[word].keys():
        if article_id == 'total_weight':
            continue
        articles.append(article_id)
    #for key in lemmas.keys():
    #    if key == word:

    return (word, articles)

#readXML('lemmas.xml')