import numpy as np

def trans(arr):
    return np.transpose(arr)

def flatt(arr):
    return arr.flatten()


n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

A = np.array(A)

print(trans(A))
print(flatt(A))