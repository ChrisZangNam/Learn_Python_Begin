#Cu phap de lap: numpy.nditer

import numpy as np

#mang 1 chieu
number_1D = np.arange(10)
print(number_1D)
for item in np.nditer(number_1D):
    print item,

#mang 2 chieu
number_2D = np.arange(0, 60, 5)
number_2D = number_2D.reshape(3, 4)

print('\nOriginal array is: ')
print(number_2D)
print('\nModified array is:')
for x in np.nditer(number_2D):
    print x,

#mang 3 chieu
number_3D = np.random.random((2, 3, 2))
print('\nOriginal array is: ')
print(number_3D)
print('\nModified array is:')
for x in np.nditer(number_3D):
    print x,

#Tranpose array (matrix):
print('\nOrginal matrix is: ')
print(number_2D)
print('\nTranpose of the original array is: ')
b = number_2D.T #Tranpose the matrix
print(b)
print('\nModified array is: ')
for x in np.nditer(b):
    print x,

print('\n')
c = b.copy(order='C')
print(c)
print('Sort in C stype: ')
for x in np.nditer(c):
    print x,
print('\n')
c = b.copy(order='F')
print(c)
print('Sort in F stype: ')
for x in np.nditer(c):
    print x,

print('\nOther method')
for x in np.nditer(b, order='C'):
    print x,

print('\n\nSua doi gia tri trong mang khi lap: \n')
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('\nOriginal array is:')
print(a)
print('\nModified array is:')

# them co readwrite de bat che do co the thay doi cac phan tu trong mang
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x
print(a)

#external loop: Lap qua dong
float_2D = np.random.random((2, 2))
print('\nOriginal array is: ')
print(float_2D)
print('\nF-stype:')
#print each column
for x in np.nditer(float_2D, flags=['external_loop'], order='F'):
    print x,

print('\nC-stype: ')
for x in np.nditer(float_2D, flags=['external_loop'], order='C'):
    print x,

#Broadcasting Iteration
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('\n\nFrist array is:')
print(a)
print('\nSecond array:')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')

print('Modified array is:')
for x, y in np.nditer([a, b]):
    print "%d:%d" %(x,y),
