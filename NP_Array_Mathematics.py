from numpy import *
n,m = map(int, input().split())
a =[]
b =[]
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

a = array(a)
b = array(b)

print(add(a, b))
print(subtract(a,b))
print(multiply(a,b))
print(a//b)
print(mod(a,b))
print(power(a,b))