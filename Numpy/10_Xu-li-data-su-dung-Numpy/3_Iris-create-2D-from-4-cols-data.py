import numpy as np

#do du lieu
iris_1d = np.genfromtxt('iris.csv', delimiter=',', dtype=None)

#Cach 1: Bien doi moi hang thanh list roi lay 4 phan tu dau
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])

#in 4 dong dau
print(iris_2d[:4])

#Cach 2: Trich xuat 4 cot dau khi doc file, chi dinh dtype=float
iris_2d = np.genfromtxt('iris.csv', delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

print(iris_2d[:4])
