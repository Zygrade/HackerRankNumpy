import numpy as np

n, m = map(int, input().split())

print(np.max(np.min(np.array([input().split() for i in range(n)], dtype=np.int), axis=1)))