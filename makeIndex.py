from nltk.stem import WordNetLemmatizer
import nltk
import os
lematizer = WordNetLemmatizer()
for i in range(0, 1):
    file_name = './dataset/rfc'+str(i)+'.txt'
    f = open(file_name, mode='r')
    doc = f.read()
    doc = doc.lower()
    tokens = nltk.tokenize.word_tokenize(doc)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [lematizer.lemmatize(
        token) for token in tokens if token.isalnum() and token not in stop_words]
    words = list(set(words))
    print(words)
