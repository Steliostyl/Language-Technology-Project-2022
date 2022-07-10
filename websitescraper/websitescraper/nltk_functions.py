import functions
import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer as punkt_sent_tok

example_text = "Hello Mr. Styl, how are you doing today? The weather is decent and Stelios is awesome. Elisavet is sleeping and I should wake her up in 30 minutes."

# Probably not useful
def tokenize_articles(articles):
    for index, article in enumerate(articles):
        # Get separate sentences in each article
        sentences = sent_tokenize(articles)
    return sentences

# Not useful
def filter_stop_words(tokenized_sentence):
    # If sentence has not already been tokenized, tokenize sentence
    if type(tokenized_sentence) != list:
        tokenized_sentence = word_tokenize(tokenized_sentence)
    return [w for w in tokenized_sentence if not w in set(stopwords.words("english"))]

# PoS Tagging
def pos_tag(article):
    #for par in article.paragraphs:
        #print(type(par['Paragraphs']), par['Paragraphs'])
        #sentences = ' '.join([str(item) for item in par['Paragraphs']])
        #tokenized = sent_tokenize(sentences)
        #article.pos_tags.append(process_content(tokenized))
        #print(tagged)
        #functions.saveEntryToCSV(article)
    tokenized = sent_tokenize(' '.join([str(item) for item in article.paragraphs]))
    article.pos_tags.append(process_content(tokenized))
    functions.saveEntryToJSON(article)
    #article.printArticle()
    #return article

def process_content(tokenized):
    tagged = []
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged.append(nltk.pos_tag(words))
            #print(tagged)
        return(tagged)

    except Exception as ex:
        print(str(ex))

#pos_tag(example_text)
