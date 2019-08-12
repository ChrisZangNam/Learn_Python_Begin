#Cau 13: Lay mau ngau nhien cot species cua mang iris
#sao cho so luong chon setose gap doi do luong cua versicolor va virginica

import numpy as np

iris_2d = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

#lay cot species tu iris
species = iris_2d[:, 4]

# Cach 1: Tao xs voi Iris-setosa(50%), Iris-versicolor(25%), Iris-virginica(25%)
label = np.array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
out = np.random.choice(label, 30, p=[0.5, 0.25, 0.25])
# print(out)

#Cach 2: Lay mau xs
#Tao 10 so tu 0->0.5, 10 so tu 0.5->0.75, 10 so tu 0.75->1.0 thanh mot mang 30

probs = np.r_[np.linspace(0, 0.500, num=10),
              np.linspace(0.501, 0.750, num=10),
              np.linspace(0.751, 1.0, num=10)]

#Lay ngau nhien mang gom 30 phan tu chi so tu mang xac suat probs gom:
index = np.searchsorted(probs, np.random.random(30))

#Tao mau can tim duoc lay tu mang pecies voi index sau khi searchsorted
out = species[index]
print(np.unique(out, return_counts=True))
