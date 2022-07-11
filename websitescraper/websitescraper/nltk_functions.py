import functions
import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer as punkt_sent_tok

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
    tokenized = sent_tokenize(article.paragraphs)
    article.pos_tags.append(process_content(tokenized))
    functions.saveEntryToJSON(article)

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
