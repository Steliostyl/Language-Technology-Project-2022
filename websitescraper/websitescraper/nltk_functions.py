import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import functions
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from pprint import pprint
from thefuzz import fuzz

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
    proper_tag = [tag][0][0][0]
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
                # Filter words that have not
                # been tagged with a closed 
                # category tag
                if tag[1] not in oc_categories:
                    continue

                # Filter unwanted symbols
                if len(tag[0]) == 1:
                    utf_8_bytes = bytes(tag[0], 'utf-8')
                    temp = []
                    for byte in utf_8_bytes:
                        temp.append(byte)
                    #                    Numbers                      Capital Letters                    Small Letters
                    if temp[0] not in range(48, 58) and temp[0] not in range(64, 91) and temp[0] not in range(97, 123):
                        #print(tag[0])
                        continue

                # Add tag to filtered_pos
                article_w_count += 1
                filtered_pos.append(tag)
                lemma = lemmatizer.lemmatize(tag[0], pos= get_wordnet_pos(tag[1])).lower()

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

def dict_sort(dict):
    # Sort answer documents by weight
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get, reverse=True)
    for key in sorted_keys:
        sorted_dict[key] = dict[key]
    return sorted_dict   

def nltk_query(lemmas, query):
    lemmatizer = WordNetLemmatizer()
    answer = {}
    for word in [query]:
        token = nltk.tag.pos_tag([word])[0]
        qword_lemma = lemmatizer.lemmatize(token[0], pos= get_wordnet_pos(token[1]))            
        #print(word, ' -> ', qword_lemma)
        for lemmas_key, lemmas_value in lemmas.items():
            ratio = fuzz.ratio(qword_lemma, lemmas_key)
            if ratio < 90:
                continue
            #print('Similarity between the words ', qword_lemma, ' and ', lemmas_key)#, ': ', ratio)
            for article, weight in lemmas_value.items():
                if article in answer:
                    answer[article] += weight
                else:
                    answer[article] = weight
                    
    return dict_sort(answer)