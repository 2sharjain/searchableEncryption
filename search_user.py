# %%
from owner_encyrpt import *
from makeIndex import *
print("hello")
S, M1_inv, M2_inv, dictionary, index = driver_owner()
print("here")
n = len(dictionary)
U = 0

def generate_trapdoor(query):

    for i in range(0,U+1):
        k = random.randint(0,1000)
        query = np.append(query, k%2)

    for i in range(0, n+U+1):
        q1 = [0]*(n+U+1)
        q2 = [0]*(n+U+1)

        if S[i] == 1:
            q1[i] = query[i]
            q2[i] = query[i]
        else:
            q1[i] = random.random()
            q2[i] = query[i] - q1[i]
            
    trapdoor = np.array([np.dot(M1_inv, q1), np.dot(M2_inv, q2)])
    
    return trapdoor

def evaluate(index, q):

    ans = []
    di = 0
    for doc in index:
        a = np.dot(q[0],doc[0])
        b = np.dot(q[1],doc[1])
        score = a+b
        if score!=0:
            heapq.heappush(ans, (score, "doc"+str(di)))
        di+=1

    return heapq.nlargest(5, ans)

    



query = "raining"
query = list(count_vectorize_query(vectorize(query), dictionary).values())
td = generate_trapdoor(query)
evaluate(index, td)

# %%
