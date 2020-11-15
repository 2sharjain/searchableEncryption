# %%
from owner_encyrpt import *
from makeIndex import *
S, M1_inv, M2_inv, dictionary, index = driver_owner()
n = len(dictionary)
U = 5
print(np.add(np.dot(M1_inv, index[0][0]),np.dot(M2_inv, index[0][1])))

#%%
q = "raining in darkness"
q = vectorize_query(q, dictionary)
q = list(q.values())
# %%
