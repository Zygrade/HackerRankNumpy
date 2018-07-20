import numpy

def arrays(arr):
    return numpy.flip(numpy.array(arr, float), 0)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)