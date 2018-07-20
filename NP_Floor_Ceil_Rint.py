import numpy as np

np.set_printoptions(sign=' ')
a= (np.array(input().split(), dtype = np.float))

print(np.floor(a) ,np.ceil(a) ,np.rint(a), sep='\n')