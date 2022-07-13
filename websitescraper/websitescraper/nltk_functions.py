import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import functions

cc_categories = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT',
'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']

# Probably not useful
def filter_stop_words(tokenized_sentence):
    # If sentence has not already been tokenized, tokenize sentence
    if type(tokenized_sentence) != list:
        tokenized_sentence = word_tokenize(tokenized_sentence)
    return [w for w in tokenized_sentence if not w in set(stopwords.words("english"))]

# PoS Tagging
def pos_tag(articles):
    pos_tags = []
    for article in articles:
        # Tokenize words in each sentence of the paragraphs
        tokenized = sent_tokenize(article['paragraphs'])
        pos_tag = process_content(tokenized)
        pos_tags.append(pos_tag)
    pos_tags_no_s_w = filter_stop_words_2(pos_tags)
    return pos_tags, pos_tags_no_s_w

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

def filter_stop_words_2(pos_tags):
    pos_no_stopwords = []
    
    for article in pos_tags:
        for sent in article:
            pos_no_stopwords.append([p_t for p_t in sent if not p_t[1] in cc_categories])

    return pos_no_stopwords