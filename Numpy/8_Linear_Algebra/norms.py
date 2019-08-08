#Norm la chieu dai cua mot vecto

import numpy as np
from numpy import linalg

A = np.array([1, 2, 3, 4, 5])
print(A)
print('Length of vector A is: ')
print(linalg.norm(A))

#L1 norm: tong gia tri tuyet doi cac gia tri cua vecto
B = np.array([6, 20, 10, -4])
print(B)
print('Sum of abs elements of vector B is: ')
print(linalg.norm(B, ord=1))
