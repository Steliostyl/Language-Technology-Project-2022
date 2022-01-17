import json

class Article:
    def __init__(self, title, details, note):
        self.title = title
        self.details = details
        self.note = note
    def printArticle(self):
        print("\nTitle:", "\n" + self.title + "\n")
        print("Details:", "\n" + self.details, "\n" + temp_note[0], "\n" + temp_note[1] + "\n")
        print(temp_text)

file = open('cnn_spider.json')
init_dict = json.load(file)
temp_text = []
temp_details = ''
temp_note = None
for a in init_dict:
    try:
        temp_text.append(a['text'])
    except:
        try:
            temp_title = a['article_title'][0]
        except:
            try:
                for i in range(0,len(a['story_details'])):
                    temp_details = temp_details + a['story_details'][i] + "\n"
            except:
                temp_note = (a['note_title'][0],a['note_text'][0])
        
new_article = Article(temp_title, temp_details, temp_note)
new_article.printArticle()

#print(type(temp_title))
#print(temp_title,"\n",temp_details,"\n",temp_note[0],"\n",temp_note[1],"\n",temp_text)