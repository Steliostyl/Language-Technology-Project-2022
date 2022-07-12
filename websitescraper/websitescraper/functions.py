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
    empty_pars = 0
    for article in init_dict:
        if len(article['paragraphs']) > 0:
            paragraphs = ''
            for paragraph in article['paragraphs']:
                paragraphs += ' ' + extract_text(paragraph)         
            article['article_datetime'] = readDateTimeFromString(article['article_datetime'])
            #article['paragraphs'] = ' '.join(paragraphs)
            article['paragraphs'] = paragraphs
            file.close()
            
            article_list.append(article)
        else:
            empty_pars += 1
    return article_list

def saveArticlesToJSON(articles):
    file = open('processed_articles.json', 'a')
    for article in articles:
        json.dump(article, file, indent=4, default=str)
        file.write(',')
    file.close()

def createNewJSONforProcessedArticles(filename):
    # Check if the file exists
    if(os.path.isfile(filename)):
        # Remove file
        os.remove(filename)
    with open('processed_articles.json', 'w') as file:
        file.write('{\t"articles": [\n')

def readArticlesFromJSON(filename):
    with open(filename, 'r') as file:
        articles = json.load(file)["articles"]
    return articles

def cleanupJSONfile():
    with open('processed_articles.json', 'rb+') as file:
        file.seek(-1, os.SEEK_END)
        file.truncate()

    with open('processed_articles.json', 'a') as file:
        file.write('\n]\n}')
#print(readArticleFromJSON('processed_articles.json')[0]["paragraphs"])
#articles = readScraperJSON('websitescraper/cnbc_spider_new.json')
#print(articles[0])

with open('processed_articles.json', 'r') as file:
    articles = json.load(file)["articles"]

for key in articles[0].keys():
    if key != 'pos_tags':
        print(key, '\n', articles[0][key], '\n')