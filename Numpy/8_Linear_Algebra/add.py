#Phep cong ma tran va vector

import numpy as np

A = np.array([
    [1, 3],
    [1, 0],
    [1,2]
])
B = np.array([
    [0, 0],
    [7, 5],
    [2,1]
])

C = A + B
print('A+B = ')
print(C)
C = np.add(A, B)
print('A+B = ')
print(C)
print('A-B= ')
C = A - B
print(C)
