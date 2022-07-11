import json
from datetime import datetime
from html_text import extract_text
import os

class Article:
    def __init__(self, title, tag, date, author, unprocessed_text, url, id):
        self.title = title
        self.url = url
        self.tag = tag
        self.date = date
        self.author = author
        self.paragraphs = ''
        self.id = id
        self.pos_tags = [] # List of tagged sentences

        # Join the text of the article into 1 string
        self.paragraphs = ''.join(unprocessed_text)

    def printArticle(self):
        print(self.id)
        print(self.url)
        print(self.title)
        print(self.tag)
        print(self.date.strftime("%A, %d %B %Y %H:%M:%S"))
        print(self.author)
        print(self.paragraphs)
        print(self.pos_tags)
        print("\n")

# Turns datetime string (mainly from html element attribute) into datetime objects
def readDateTimeFromString(datetimeString):
    return datetime.fromisoformat(datetimeString[:-2] + ":" + datetimeString[len(datetimeString)-2:])

# Function to read the articles from the JSON file and create Article objects from them
def readJSON(filename):
    article_list = []
    file = open(filename)
    init_dict = json.load(file)
    for index, article in enumerate(init_dict):
        if len(article['paragraphs']) > 0:
            paragraphs = []
            for paragraph in article['paragraphs']:
                paragraphs.append(extract_text(paragraph))
            new_article =  Article(article['article_title'], article['article_tag'], readDateTimeFromString(article['article_datetime']), article['author'],paragraphs,article['url'], index)
            file.close()
            article_list.append(new_article)
    return article_list

def saveEntryToJSON(article):
    with open('processed_articles.json', 'a') as outfile:
        json.dump(article.__dict__, outfile, indent=4, default=str)

def deleteFile(filename):
    # Check if the file exists
    if(os.path.isfile(filename)):
        # Remove file
        os.remove(filename)