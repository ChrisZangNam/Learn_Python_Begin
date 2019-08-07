'''
Tao mang co cac gia tri bang nhau:
    - empty(): tao mang chua duoc khoi tao voi cac gia tri ngau nhien
            numpy.empty(shape, dtype = float, order = 'C')

    - zeros(): tao ra mang cac gia tri deu = 0
            numpy.zeros(shape, dtype = float, order = 'C')

    - ones() : tao ra mang cac gia tri deu = 1
            numpy.ones(shape, dtype = None, order = 'C')

    - full() : tao ra mang cac gia tri bang mot so cho truoc

Dau vao la shape cua array duoi daang tuple va gia tri cho truoc(neu co)
'''

import numpy as np

x = np.empty([3, 2], dtype=int)
print(x)

#a. Mang 1 chieu

number_1D_zeros = np.zeros(7)  #np.zeros((7,))
print('\n')
print(number_1D_zeros)

number_1D_ones = np.ones(3)
print('\n')
print(number_1D_ones)

number_1D_sevens = np.full((6,), 7)
print('\n')
print(number_1D_sevens)

#b. Mang 2 chieu
number_2D_zeros = np.zeros((7,7))
print('\n')
print(number_2D_zeros)

number_2D_ones = np.ones((6,5))
print('\n')
print(number_2D_ones)

number_2D_sevens = np.full((6,6), 8)
print('\n')
print(number_2D_sevens)

#c. Mang 3 chieu
number_3D_zeros = np.zeros((4,2,3))
print('\n')
print(number_3D_zeros)

number_3D_ones = np.ones((2, 5,4))
print('\n')
print(number_3D_ones)

number_3D_sevens = np.full((3,4,7), 9)
print('\n')
print(number_3D_sevens)

'''
np.eye() : tao mot ma tran don vi (nxn)
'''
x = np.eye((10), dtype=int)
print('\n')
print(x)
