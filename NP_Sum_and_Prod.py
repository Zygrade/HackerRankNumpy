from numpy import *

n,m = map(int, input().split())

print(prod(sum(array([input().split() for i in range(n)], dtype= int), axis =0)))