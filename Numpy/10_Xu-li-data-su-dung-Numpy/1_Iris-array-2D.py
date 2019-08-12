#Cau 1: Doc du lieu iris dung ham np.genfromtxt() voi dtype='object'.
# Du lieu tra ve mot mang 2 chieu, voi cac phan tu co kieu byte.

import numpy as np

#Cho dtype='object', magn 2 chieu lieu byte duoc tra ve
iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

print(iris.shape)

#Lay mot dong du lieu
a_row = iris[1]
print(a_row)

#in kieu du lieu cho tung phan tu
for i in range(5):
    print(a_row[i], type(a_row[i]))
