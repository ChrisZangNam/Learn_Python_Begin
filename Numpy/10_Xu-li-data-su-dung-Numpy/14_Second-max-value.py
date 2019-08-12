#Cau 14: tim gia tri lon thu 2 cua petallength trong nhom setora

import numpy as np

iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

#tao mang moi nhom boi gia tri sotera
setosa = iris[iris[:, 4] == b'Iris-setosa']
print(setosa.shape)

#chi lay cot 2 roi chuyen thanh kieu float
petallength_setosa = setosa[:, 2].astype(float)

#lay gia tri lon thu 2 cua mang
out = np.unique(np.sort(petallength_setosa))[-2]
print(out)
