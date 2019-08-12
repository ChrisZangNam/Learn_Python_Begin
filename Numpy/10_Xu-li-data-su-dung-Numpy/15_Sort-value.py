#Cau 15: Sap xep tap du lieu iris dua tren cot sepallength

import numpy as np

iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

#Sap xep cot 0
out = iris[iris[:, 0].argsort()]
print(out[:5])
