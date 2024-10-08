from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity
from time import perf_counter

start_time = perf_counter()
count_Vectorizer = CountVectorizer()
tf_idf_Transformer = TfidfTransformer()

def vectorize_Documents(dataset):
    """Finds features of a document dataset and 
    transforms documents to feature vectors, using
    tf-idf"""
    # CountVectorizer does the preprocessing, tokenization and stopword filtering 
    # and builds a feature dictionary, transforming documents to feature vectors.
    features_count = count_Vectorizer.fit_transform(dataset.data)

    # TfidfTransformer is used to transform the count of features to tf-idf
    # in each vector.
    features_tfidf = tf_idf_Transformer.fit_transform(features_count)
    return features_tfidf

def train_Classifier(d_categories, tf_idf_vector):
    """Trains a model to classify categories using their feature vector"""
    t_classifier = MultinomialNB().fit(tf_idf_vector, d_categories)
    return t_classifier

def predict_Category_Clf(documents, classifier, print=False):
    """Predicts the category of a list of documents"""

    features_count = count_Vectorizer.transform(documents)
    features_tfidf = tf_idf_Transformer.transform(features_count)
    predicted = classifier.predict(features_tfidf)
    
    if(print):
        for doc, category in zip(documents, predicted):
            print('%r\n%s\n' % (doc, twenty_news_train.target_names[category]))

def find_Category(train, doc):
    max_sim = 0
    for document in train:
        sim = cosine_similarity(document, doc)
        if sim > max_sim:
            max_sim = sim
    print(max_sim)
    diff = 0
    return diff

def predict_Category_custom(test_data, train_vector):
    features_count = count_Vectorizer.transform(test_data)
    features_tfidf = tf_idf_Transformer.transform(features_count)
    for doc in features_tfidf:
        find_Category(train_vector, doc)

    return

# Read dataset and load it into variable
twenty_news_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=21)

# Vectorize dataset
tf_idf_vect = vectorize_Documents(twenty_news_train)

# Train classifier to later predict article category
classifier = train_Classifier(twenty_news_train.target, tf_idf_vect)

# Predict category of test documents from the dataset
twenty_news_test = fetch_20newsgroups(subset='test', shuffle=True, random_state=21)
#predict_Category_Clf(twenty_news_test.data, classifier)
print(tf_idf_vect.shape)
predict_Category_custom(twenty_news_test.data, tf_idf_vect)

# Measure the performance of model
finish_time = perf_counter()
e_time = finish_time - start_time
print("Articles:", len(twenty_news_test.data), "\nElapsed time:", e_time)