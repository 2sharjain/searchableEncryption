# %%
from nltk.stem import WordNetLemmatizer
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import heapq
import os.path
from nltk.stem import PorterStemmer 

ps = PorterStemmer()

def vectorize(str):
    tokens = nltk.tokenize.word_tokenize(str)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [ps.stem(token) for token in tokens if token.isalpha() and token not in stop_words]
    return words

def gen_corpus(N):
    corpus =[]
    for i in range(0, N):
        file_name = './dataset/rfc'+str(i)+'.txt'
        f = open(file_name, mode='r')
        doc = f.read()
        doc = doc.lower()
        vectorized_word = vectorize(doc)
        s = ""
        for word in vectorized_word:
            s += word
            s += " "
        corpus.append(s)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    dictionary = vectorizer.get_feature_names()
    file_index = ['doc' + str(i) for i in range(0, N)]
    count_df = pd.DataFrame(data=X.toarray(), index=file_index, columns=dictionary)
    return count_df



def count_vectorize_query(Q, dictionary):
    c_vector = dict()
    for term in dictionary:
        c_vector[term] = 1 if term in Q else 0
    return c_vector


def evaluate_query(corpus_index, query):
    ans = []
    query = np.array(query)
    di = 0
    for doc in corpus_index:
        doc = np.array(doc).reshape(len(doc),1)
        score = np.asscalar(np.dot(query.T, doc))
        if score!=0:
            heapq.heappush(ans, (score,"doc"+str(di)))

        di+=1
    
    return heapq.nlargest(5, ans)

def driver():

    count_df = gen_corpus(10)
    dictionary = list(count_df.columns)
    len(dictionary)
    corp = count_df.to_numpy()
    query = "raining darkness"
    query = vectorize(query)
    query = count_vectorize_query(query, dictionary)
    query = np.array(list(query.values())).reshape((len(query),1))
    return evaluate_query(corp, query)

driver()



# %%
