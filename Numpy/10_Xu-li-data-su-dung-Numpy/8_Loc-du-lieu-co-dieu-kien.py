#Cau 8: doc 4 cot du lieu dau tien, loc cac dong co
#petallength(cot  3) >1,5 va sepallength(cot 1) <5.

import numpy as np

#doc du lieu
iris_2d = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0, 1, 2, 3])

#dieu kien lay du lieu
condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)

#Lay du lieu
out = iris_2d[condition]
print(out)
