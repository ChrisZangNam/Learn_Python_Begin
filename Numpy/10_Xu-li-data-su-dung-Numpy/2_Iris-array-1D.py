#Cau 2: Doc du lieu Iris dung np.genfromtxt() voi dtype=None.
#Du lieu tra ve mang 1 chieu voi cac phan tu kieu tuple.
#Trong moi tuple, so co kieu float va chuoi co kieu byte

import numpy as np

iris_1d = np.genfromtxt('iris.csv', delimiter=',', dtype=None)
print(iris_1d.shape)

#Lay mot dong du lieu
a_row = iris_1d[1]
print(a_row)

#in kieu du lieu cho tung phan tu cua tuple
for i in range(5):
    print(a_row[i], type(a_row[i]))
