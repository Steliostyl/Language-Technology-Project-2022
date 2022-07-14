import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

cc_categories = ['CD', 'CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT',
'POS', 'PRP', 'PRP$', 'RP', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB']

oc_categories = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'NN', 'NNS',
'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'FW']

# PoS Tagging
def pos_tag(articles):
    pos_tags = []
    for article in articles:
        # Tokenize words in each sentence of the paragraphs
        tokenized = sent_tokenize(article['paragraphs'])
        pos_tag = process_content(tokenized)
        pos_tags.append(pos_tag)
    return pos_tags, filter_stop_words(pos_tags)

# Where the actual pos_tagging happens
def process_content(tokenized):
    try:
        tagged = []
        # PoS tag every tokenized sentence
        for sent in tokenized:
            words = word_tokenize(sent)
            tagged.append(nltk.pos_tag(words))
        return(tagged)

    except Exception as ex:
        print(str(ex))

def get_wordnet_pos(tag):
    #"""Map POS tag to first character lemmatize() accepts"""
    #tag = nltk.pos_tag([word])[0][1][0].upper()
    #print(type([tag]))
    proper_tag = [tag][0][0][0]
    #print(proper_tag)
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(proper_tag, wordnet.NOUN)


def filter_stop_words(pos_tags):
    pos_no_stopwords = []
    lemmas = {}
    articles_w_count = []
    lemmatizer = WordNetLemmatizer()
    
    for id, article in enumerate(pos_tags):
        article_pos_no_sw = []
        filtered_pos = []
        article_w_count = 0
        for sent in article:
            for tag in sent:
                if tag[1] in oc_categories:
                    # Add tag to filtered tags
                    article_w_count += 1
                    filtered_pos.append(tag)
                    lemma = lemmatizer.lemmatize(tag[0], pos= get_wordnet_pos(tag[1]))
                    # If lemma doesn't already exist 
                    # in the lemmas dict, create it
                    # and set the count for the 
                    # corresponding article to 1
                    if lemma not in lemmas.keys():
                        lemmas[lemma] = {
                            id: 1
                        }
                    # If lemma has already been added
                    # to the dict
                    else:
                        # If lemma has previously been found in 
                        # the same article, increase its count
                        if id in lemmas[lemma].keys():
                            lemmas[lemma][id] += 1
                        # Otherwise, create a new entry for this
                        # article and initialize its count to 1
                        else:
                            lemmas[lemma][id] = 1
            article_pos_no_sw.append(filtered_pos)
        articles_w_count.append(article_w_count)
        pos_no_stopwords.append(article_pos_no_sw)

    return pos_no_stopwords, articles_w_count, lemmas