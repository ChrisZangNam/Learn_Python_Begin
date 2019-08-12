#Cau 9: tim moi tuong quan giuwa sepallength(cot 1) va petallength(cot 3)

import numpy as np

iris_2d = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0, 1, 2, 3])

#Cach 1: dung ham corrcoef tu numpy
out = np.corrcoef(iris_2d[:, 0], iris_2d[:, 2])[0,1]
print(out)

#Cach 2: dung ham pearsonr tu scipy
from scipy.stats.stats import pearsonr
out = pearsonr(iris_2d[:, 0], iris_2d[:, 2])[0]
print(out)
