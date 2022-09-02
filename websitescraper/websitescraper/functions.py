import json
from xml.dom import minidom
import math
import xml.etree.ElementTree as ET

# Read the articles from JSON file
def readJSON(filename):
    with open(filename, 'r') as file:
        articles = json.load(file)
    return articles

# Write article list to JSON file
def saveDictToJSON(input_Dict, filename):
    # Open the file with filename (if it exists, it gets 
    # overwritten because of the use of w instead of a)
    with open(filename, 'w') as file:
        json.dump(input_Dict, file, indent=2, default=str)
    file.close()

# Calculate weights for all lemmas (using tf_idf)
def calculateTFidf(lemmas, article_w_count):
    article_count = len(article_w_count)
    for lemma in lemmas:
        # IDF of each lemma is equal to the base 2 log of the
        # article count of our database devided by the count
        # of articles the lemma is present in
        idf = math.log2(article_count/len(lemmas[lemma].keys()))
        for key in lemmas[lemma].keys():
            tf = lemmas[lemma][key]/article_w_count[key]
            tf_idf = tf*idf
            lemmas[lemma][key] = tf_idf

    return lemmas

# Create and save XML file from lemmas dict
def createXML(lemmas_dict):
    root = minidom.Document()
    inv_index = root.createElement('inverted_index')
    root.appendChild(inv_index)

    for word in lemmas_dict.keys():
        new_lemma = root.createElement('lemma')
        new_lemma.setAttribute('name', word)
        for key in lemmas_dict[word].keys():
            new_document = root.createElement('document')
            new_document.setAttribute('url', str(key))
            new_document.setAttribute('weight', str(lemmas_dict[word][key]))
            new_lemma.appendChild(new_document)
        inv_index.appendChild(new_lemma)

    xml_str = root.toprettyxml(indent ='\t')
    
    with open('lemmas.xml', "w", encoding='utf-8') as file:
        file.write(xml_str) 

# Read XML file containing lemmas and load it to a dict
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
        
    return lemma_dict