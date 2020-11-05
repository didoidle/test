import numpy as np

a = np.empty([0, 2])
b = np. array([[1, 2], [1, 2]])
c = b+b
print(b[:, 0:1])
#np.vstack((a,b))
print (c)
for i in range(np.shape(b)[0]):
    print(i)