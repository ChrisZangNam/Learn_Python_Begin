#Cau 10: Tim cac gia tri duy nhat va so luong cac gia tri duy nhat trong cot species

import numpy as np

#doc du lieu chuyen sang mang 1 chieu
iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

#sd ham unique
out = np.unique(iris[:, 4], return_counts=True)
print(out)
