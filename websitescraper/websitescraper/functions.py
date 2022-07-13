import json
from datetime import datetime
from html_text import extract_text
import os

# Turns datetime string (mainly from html element attribute) into datetime objects
def readDateTimeFromString(datetimeString):
    return datetime.fromisoformat(datetimeString[:-2] + ":" + datetimeString[len(datetimeString)-2:])

# Function to read the articles from the JSON file that 
# the scraper createdand create Article objects from them
def readScraperJSON(filename):
    article_list = []
    file = open(filename)
    init_dict = json.load(file)
    index = 0

    for article in init_dict:
        if len(article['paragraphs']) > 0:
            paragraphs = ''
            for paragraph in article['paragraphs']:
                paragraphs += ' ' + extract_text(paragraph)         
            article['article_datetime'] = readDateTimeFromString(article['article_datetime'])
            #article['paragraphs'] = ' '.join(paragraphs)
            article['paragraphs'] = paragraphs
            article['id'] = index
            file.close()
            article_list.append(article)
            index += 1
    return article_list

def saveArticlesToJSON(articles, filename):
    file = open(filename, 'a')
    for article in articles:
        json.dump(article, file, indent=4, default=str)
        file.write(',')
    file.close()

def createNewJSON(filename):
    # Check if the file exists
    if(os.path.isfile(filename)):
        # Remove file
        os.remove(filename)
    with open(filename, 'w') as file:
        file.write('{\t"articles": [\n')

def readArticlesFromJSON(filename):
    with open(filename, 'r') as file:
        articles = json.load(file)["articles"]

    # Check if function works correctly
    # for key in articles[0].keys():
    #     if key != 'pos_tags':
    #         print(key, '\n', articles[0][key], '\n')

    return articles

def cleanupJSONfile(filename):
    with open(filename, 'rb+') as file:
        file.seek(-1, os.SEEK_END)
        file.truncate()

    with open(filename, 'a') as file:
        file.write('\n]\n}')