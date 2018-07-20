import numpy as np

n= int(input())
A = np.array([input().split() for _ in range(n)] , dtype= np.float)

np.set_printoptions(legacy='1.13')

print(np.linalg.det(A))