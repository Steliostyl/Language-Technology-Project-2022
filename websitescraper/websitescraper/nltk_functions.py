import functions
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer as punkt_sent_tok

cc_categories = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT',
'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']

# Probably not useful
def filter_stop_words(tokenized_sentence):
    # If sentence has not already been tokenized, tokenize sentence
    if type(tokenized_sentence) != list:
        tokenized_sentence = word_tokenize(tokenized_sentence)
    return [w for w in tokenized_sentence if not w in set(stopwords.words("english"))]

# PoS Tagging
def pos_tag(article):
    # Tokenize words in each sentence of the paragraphs
    tokenized = sent_tokenize(article['paragraphs'])
    article['pos_tags'] = process_content(tokenized)

# Where the actual pos_tagging happens
def process_content(tokenized):
    try:
        tagged = []
        # PoS tag every tokenized sentence
        for sent in tokenized:
            words = nltk.word_tokenize(sent)
            tagged.append(nltk.pos_tag(words))
        return(tagged)

    except Exception as ex:
        print(str(ex))

def filter_stop_words_2(articles):
    #print(articles[0]['pos_tags'])
    for article in articles:
        article['pos_tags_no_stopwords'] = []
        for sent in article['pos_tags']:
            article['pos_tags_no_stopwords'].append([p_t for p_t in sent if not p_t[1] in cc_categories])