import json
from datetime import datetime
from html_text import extract_text

class Article:
    def __init__(self, title, tag, date, author, next_paragraphs_topic, first_par_after_top_change, unprocessed_text, url, id):
        self.title = title
        self.url = url
        self.tag = tag
        self.date = date
        self.author = author
        self.next_paragraphs_topic = next_paragraphs_topic
        self.first_par_after_top_change = first_par_after_top_change
        self.id = id
        
        # Initialize paragraphs variables
        final_paragraphs = []
        new_paragraphs = []
        new_topic = ''
        t = 0

        # Connect strings in the same paragraphs, add headers (topics) if available
        if len(next_paragraphs_topic) > 0:
            # Crawler has found headers
            for i in range(0,len(unprocessed_text)):
                # Topic changes, assign past paragraphs to previous topic and reset new_topic variable
                if unprocessed_text[i] in first_par_after_top_change:
                    final_paragraphs.append({'Topic': new_topic, 'Paragraphs': new_paragraphs})
                    new_topic = next_paragraphs_topic[t]
                    t += 1
                    new_paragraphs = []
                new_paragraphs.append(unprocessed_text[i])
        else:
            # Crawler has NOT found headers
            for txt in unprocessed_text:
                new_paragraphs.append(txt)
        final_paragraphs.append({'Topic': new_topic, 'Paragraphs': new_paragraphs})

        self.paragraphs = final_paragraphs

    def printArticle(self):
        print(self.id)
        print(self.url)
        print(self.title)
        print(self.tag)
        print(self.date.strftime("%A, %d %B %Y %H:%M:%S"))
        print(self.author)
        for paragraph in self.paragraphs:
            print("\n---------------" + paragraph['Topic'] + "---------------")
            if type(paragraph['Paragraphs']) == list:
                for p in paragraph['Paragraphs']:
                    print(p, "\n")
            else:
                print(paragraph['Paragraphs'])
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
            new_article =  Article(article['article_title'], article['article_tag'], readDateTimeFromString(article['article_datetime']), article['author'],article['next_paragraphs_topic'],article['first_par_after_top_change'],paragraphs,article['url'], index)
            file.close()
            article_list.append(new_article)
    return article_list