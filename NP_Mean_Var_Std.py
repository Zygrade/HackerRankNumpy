import numpy as np
np.set_printoptions(legacy='1.13') #formatter to use the default settings from numpy version 1.13 instead of numpy version 1.14
n, x = map(int, input().split())
A = np.array([input().split() for i in range(n)], dtype=np.int)

print(np.mean(A, axis=1),np.var(A, axis=0),np.std(A), sep = '\n')