from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
import nltk_functions
test = "Though CPI's spike is led by energy and food prices, which are largely global problems, prices continue to mount for domestic goods and services, from shelter to autos to apparel."

# Tokenize words in each sentence of the paragraphs
tknzd = sent_tokenize(test)
# Send the tokenized words of each sentence for PoS tagging
pos_tags = nltk_functions.process_content(tknzd)
print(pos_tags[0])
for tag in pos_tags[0]:
    # Filter words that have not
    # been tagged with a closed 
    # category tag
    if tag[1] not in nltk_functions.oc_categories:
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

    lemma = WordNetLemmatizer().lemmatize(tag[0], pos= nltk_functions.get_wordnet_pos(tag[1])).lower()
    print(lemma)
#print(WordNetLemmatizer().lemmatize('democrats', pos="n"))