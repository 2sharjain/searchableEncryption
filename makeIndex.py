from nltk.stem import WordNetLemmatizer
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


lematizer = WordNetLemmatizer()
corpus = []
N = 5
for i in range(0, N):
    file_name = './dataset/rfc'+str(i)+'.txt'
    f = open(file_name, mode='r')
    doc = f.read()
    doc = doc.lower()
    tokens = nltk.tokenize.word_tokenize(doc)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [lematizer.lemmatize(
        token) for token in tokens if token.isalnum() and token not in stop_words]
    # print(words)
    s = ""
    for word in words:
        s += word
        s += " "
    # print(s)
    corpus.append(s)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

dictionary = vectorizer.get_feature_names()
file_index = ['doc' + str(i) for i in range(0, N)]
count_df = pd.DataFrame(data=X.toarray(), index=file_index, columns=dictionary)

print(count_df.head())
