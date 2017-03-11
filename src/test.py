import numpy as np

a = np.array([[1, 2], [3, 4]])
print a

b = np.zeros((2))
for i in range(2):
    b[i] = np.mean(a[i, :])
print b