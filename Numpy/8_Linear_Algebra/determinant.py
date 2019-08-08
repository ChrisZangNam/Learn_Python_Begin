#Dinh thuc cua ma tran: Chi danh cho ma tran vuong nxn
import numpy as np

A = np.array([[1, 2], [3, 4]])
print('A = ')
print(A)
print'Det(A) = ', np.linalg.det(A) #-2

B = np.array([
    [0, 2, -3, 0],
    [-2, 0, 2, 1],
    [3, -1, 0, 0],
    [4, 5, -1, 2]])
print('B = ')
print(B)
print'Det(B) = ',np.linalg.det(B) #39
