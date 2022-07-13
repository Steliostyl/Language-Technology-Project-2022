import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

cc_categories = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT',
'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']

# PoS Tagging
def pos_tag(articles):
    pos_tags = []
    for article in articles:
        # Tokenize words in each sentence of the paragraphs
        tokenized = sent_tokenize(article['paragraphs'])
        pos_tag = process_content(tokenized)
        pos_tags.append(pos_tag)
    pos_tags_no_s_w = filter_stop_words(pos_tags)
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

def filter_stop_words(pos_tags):
    pos_no_stopwords = []
    
    for article in pos_tags:
        article_pos_no_sw = []
        for sent in article:
            article_pos_no_sw.append([p_t for p_t in sent if not p_t[1] in cc_categories])
        pos_no_stopwords.append(article_pos_no_sw)

    return pos_no_stopwords