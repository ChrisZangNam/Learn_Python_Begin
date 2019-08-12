#Cau 16: Tim gia tri xuat hien nhieu nhat trong cot petallength trong tap du lieu iris.
#Lay cac phan tu duy nhat va so luong moi phan tu

import numpy as np

iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

values, counts = np.unique(iris[:,2], return_counts=True)
print(values)
print(counts)

#dung ham argmax de tim vi tri cua phan tu xuat hien nhieu nhat
print(values[np.argmax(counts)], np.argmax(counts))

