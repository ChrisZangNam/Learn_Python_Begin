'''
Phep lan truyen: Broadcasting
--> Dong loat thay doi gia tri nhieu phan tu

cu the: Numpy cho phep thuc hien tinh toan giua cac mang khac chieu voi nhau
'''
from __future__ import print_function
import numpy as np

print('1. Lan truyen voi mang so\n')

print('1.1 Cong mang voi so: ')
print('Mang mot chieu\n')
number_1D = np.array([1, 2, 3])
print(number_1D)
print('number_1D + 3 = ')
print(number_1D + 3)  #= number_1D + [3,3,3]

print('\nMang 2 chieu: \n')
number_2D = np.array([[4, 5, 6], [7, 8, 9]])
print(number_2D)
print('number_2D + 20 = ')
print(number_2D + 20)

print('\n1.2 Phep nhan mang voi so:')
print('Mang mot chieu\n')
number_1D = np.array([1, 2, 3])
print(number_1D)
print('number_1D * 3 = ')
print(number_1D * 3)

print('\nMang 2 chieu: \n')
number_2D = np.ones((8,8))
print(number_2D)
print('number_2D * 20 = ')
print(number_2D * 20)

print('\n2. Lan truyen mang voi mang\n')
print('2.1 cong 2 mang khac chieu: ')
x = np.array([[6, 9, 10], [15, 18, 20]])
y = np.array([[2], [4]])
z = [1,2,3]
print(x, end='\n+')
print(y, end='\n=')
print(x + y)
print('\n')

print(x, end='\n+')
print(z, end='\n=')
print(x + z)
