# %%
from makeIndex import *
import random
N = 10
U = 5
n = 0
S =[]
M1 = []
M2 = []
M1_inv = []
M2_inv =[]

dictionary = list()

def generate_key():
    
    global n
    S = list(np.random.randint(2, size = n+U+1))
    M1 = np.random.rand(n+U+1,n+U+1)
    M1_inv = np.linalg.inv(M1)
    M2 = np.random.rand(n+U+1,n+U+1)
    M2_inv = np.linalg.inv(M1)

    return S, M1, M2, M1_inv, M2_inv

def extend_dimension():

    global n
    global dictionary

    count_df = gen_corpus(N)
    dictionary = list(count_df.columns)
    n = len(dictionary)
    corpus = count_df.to_numpy()
    for i in range(0, U+1):
        k = random.random()
        epsilon = np.array([k for j in range(0,N)])
        epsilon = epsilon.reshape(N,1)
        corpus = np.append(corpus, epsilon, axis=1)
         
    return corpus

def split_and_encrypt(corpus):

    corpus = list(corpus)
    encrypted_corpus = []

    for doc in corpus:
        doc1 = [0]*(n+U+1)
        doc2 = [0]*(n+U+1)
        for j in range(0,n+U+1):
            if S[j] == 0:
                doc1[j] = doc[j]
                doc2[j] = doc[j]
            else:
                doc1[j] = random.random()
                doc2[j] = doc[j] - doc1[j]

        doc1_e = np.dot(M1, np.array(doc1))
        doc2_e = np.dot(M2, np.array(doc2))

        doc1_e = np.squeeze(doc1_e)
        doc2_e = np.squeeze(doc2_e)

        encrypted_corpus.append([doc1_e,doc2_e])
    
    encrypted_corpus = np.array(encrypted_corpus)
    return encrypted_corpus

def driver_owner():

    global dictionary, S, M1, M2, M1_inv, M2_inv
    corpus = extend_dimension()
    S, M1, M2, M1_inv, M2_inv = generate_key()
    encrypted_index = split_and_encrypt(corpus)
    return S, M1_inv, M2_inv, dictionary, encrypted_index

driver_owner()
print("emd")


# %%
