#CAu 4: Tim mea, median, standard deviation(do lech chuan) cua cot sepal_length cuar irsi(cot thu 1)

import numpy as np

# Trich xuat cot 1 tu IRIS thanh mang 1 chieu
sepallength = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0])

print(sepallength.shape)

#tim mean, med, sd
mean, median, std = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mean, median, std)
