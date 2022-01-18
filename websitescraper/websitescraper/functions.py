import json
from datetime import datetime 

class Article:
    def __init__(self, title, tag, date, author, paragraph_headers, paragraphs):
        self.title = title
        self.tag = tag
        self.author = author
        self.paragraph_headers = paragraph_headers
        final_paragraphs = []

        #for item in date:
        #    datetime = datetime + item + " "

        new_paragraph_text = ''
        new_paragraph_header = ''
        
        for i in range(0,len(paragraphs)):
            if paragraphs[i] in paragraph_headers:
                final_paragraphs.append({"Header": new_paragraph_header, "Text": new_paragraph_text})
                new_paragraph_text = ''
                new_paragraph_header = paragraphs[i]
            else:
                new_paragraph_text = new_paragraph_text + paragraphs[i]
                if i == len(paragraphs)-1:
                    final_paragraphs.append({"Header": new_paragraph_header, "Text": new_paragraph_text})

        self.date = date
        self.paragraphs = final_paragraphs

    def printArticle(self):
        print(self.title)
        print(self.tag)
        print(self.date.strftime("%A, %d %B %Y %H:%M:%S"))
        print(self.author)
        for paragraph in self.paragraphs:
            print(paragraph['Header'],"\n" + paragraph['Text'] + "\n")

def readDateTimeFromString(datetimeString):
    return datetime.fromisoformat(datetimeString[:-2] + ":" + datetimeString[len(datetimeString)-2:])

def readJSON(filename):
    file = open(filename)
    init_dict = json.load(file)
    new_article =  Article(init_dict[0]['article_title'], init_dict[0]['article_tag'], readDateTimeFromString(init_dict[0]['article_datetime']), init_dict[0]['author'],init_dict[0]['paragraph_headers'],init_dict[0]['paragraphs'])
    file.close()
    return new_article