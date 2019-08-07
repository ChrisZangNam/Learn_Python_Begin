# The most important object defined in NumPy ia an
# N-dimensional array type called ndarray(Mang n chieu).

#Cu phap: numpy.array
#       numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
#       object: doi tuong can tao
#       dtype: Kieu du lieu mong muon cua mang
#       copy: Doi tuong duoc sao chep
#       order:
#       subok
#       ndmin: chi dinh Kich thuoc toi thieu cua mang

import numpy as np

#mang mot chieu:
number_vector = np.array([1, 2, 3, 4])
print(number_vector)
print(number_vector.shape) #Kich thuoc cua mang

#mang 2 chieu
number_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(number_matrix)
print(number_matrix.shape)

#mang 3 chieu
number_3D_matrix = np.array([
                    [[1, 2, 3], [4, 5, 6]],
                    [[4, 5, 6], [1, 2, 3]]
                    ])
print(number_3D_matrix)
print(number_3D_matrix.shape)

#minium dimensions : toi thieu so chieu
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
print(a.shape)

#dtype parameter
a = np.array([1,2,3], dtype=complex) #Kieu so phuc
print(a)

#Resize the ndarray
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3,2)
print(b)

#an array of evenly spaced numbers: mang voi cac so cach deu nhau
a = np.arange(24) #one-dimension array
print(a)
print(a.ndim)  #so chieu cua mang

b = a.reshape(2, 4, 3) #gom 2 matrix size 4x3
print(b)
print(b.ndim)


#Tra ve do dai cua moi phan tu theo byte

#dtype of array is int8(1 byte)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize, 'byte')

#dtype of array is now float32(4byte)
x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(x.itemsize, 'byte')



#numpy.flags
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
