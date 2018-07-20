import numpy as np

n, m, p = map(int, input().split())
A = []
B =[]
for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(m):
    B.append(list(map(int, input().split())))

A = np.array(A)
B = np.array(B)

print(np.concatenate((A,B), axis=0))