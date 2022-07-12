import functions
import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer as punkt_sent_tok

# Probably not useful
def tokenize_articles(articles):
    for article in articles:
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
    tokenized = sent_tokenize(article['paragraphs'])
    article['pos_tags'] = process_content(tokenized)

def process_content(tokenized):
    try:
        tagged = []
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged.append(nltk.pos_tag(words))
        return(tagged)

    except Exception as ex:
        print(str(ex))