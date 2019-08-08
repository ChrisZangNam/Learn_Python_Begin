#Ma tra nghich dao
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)

print('X = ')
print(x)
print('Invert matrix of X = ')
print(y)
print 'dot(x, inv(x)) = '
print np.dot(x, y)

A = np.array([[1, 1, 1],
            [0, 2, 5],
            [2, 5, -1]])
print'Matrix A = '
print A
A_inv = np.linalg.inv(A)
print'Invert of A = '
print A_inv

print'Matrix B = '
B = np.array([[6], [-4], [27]])
print(B)

print('compute A-1B: ')  #Giai hpt A*X = B --> giai X
x = np.linalg.solve(A, B)
print(x)
