import numpy as np


A = np.array(input().split() , dtype= np.int)
B = np.array(input().split() , dtype= np.int)
print(np.inner(A,B))
print(np.outer(A,B))