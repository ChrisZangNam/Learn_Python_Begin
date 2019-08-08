#Cac thao tac cac phan tu trong doi tuong
import numpy as np

print('1. Thay doi kich thuoc mang')
number_2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(number_2D)
print(number_2D.shape)
print('Array 3 dimentions fromarray 2 dimention: ')
number_3D = number_2D.reshape(2, 2, 2)
print(number_3D)

print(number_3D.shape)

#flatten(): Tra ve mang duoc duoi ra con 1 chieu
number = np.random.random((3, 3, 3))
print('\nArray before changging:')
print(number)
print('\nArray 1 dimention from array before is:')
flattened_number = number.flatten()
print(flattened_number)
print(flattened_number.shape)

#expand_dims(): Tra ve mang duoc them chieu
number_2D = np.array(([1, 2], [3, 4]))
print('\nOriginal array is: ')
print(number_2D)
print(number_2D.shape)

#mo rong theo dong axis = 0
number_3D_axis_0 = np.expand_dims(number_2D, axis=0)
print('Array after explanding follow row axis=0: ')
print(number_3D_axis_0)
print(number_3D_axis_0.shape)

#mo rong theo cot axis=1
number_3D_axis_1 = np.expand_dims(number_2D, axis=1)
print('Array after explanding follow column axis=1: ')
print(number_3D_axis_1)
print(number_3D_axis_1.shape)

#squeeze(): Tra ve mang moi duoc giam chieu
number_3D = np.random.random((1, 20, 20))
print('\nOriginal array is: ')
print(number_3D)
print(number_3D.shape)

number_2D_axis_0 = np.squeeze(number_3D, axis=0)
print('Array after squeezing follow row axis=0: ')
print(number_2D_axis_0)
print(number_2D_axis_0.shape)

#Chuyen vi
number_2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('\nOriginal array: ')
print(number_2D)

print('Transpose matrix from array is : ')
print(number_2D.T)
print(np.transpose(number_2D))
