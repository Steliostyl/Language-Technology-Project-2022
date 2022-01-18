import json

class Article:
    def __init__(self, title, tag, date, author, paragraphs):
        self.title = title
        self.tag = tag
        self.author = author[0]
        datetime = ''
        paragraphs_string = ''

        for item in date:
            datetime = datetime + item + " "

        for item in paragraphs:
            paragraphs_string = paragraphs_string + item

        self.datetime = datetime
        self.paragraphs_string = paragraphs_string

    def printArticle(self):
        print(self.title, "\n" + self.tag, "\n" + self.datetime, "\n" + self.author[0], "\n" + self.paragraphs_string)

def readJSON(filename):
    file = open(filename)
    init_dict = json.load(file)
    new_article =  Article(init_dict[0]['article_title'], init_dict[0]['article_tag'], init_dict[0]['article_date'], init_dict[0]['author'],init_dict[0]['paragraphs'])
    file.close()
    return new_article

readJSON("cnn_spider.json").printArticle()