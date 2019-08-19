import numpy as np
import numpy.core.defchararray as np_f

#Lay cac dac trung va luu vao X
X = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0, 1, 2, 3], skip_header=1)
print(X.shape)

#Lay species va luu vao Y
Y = np.genfromtxt('iris.csv', delimiter=',', dtype=str, usecols=[4], skip_header=1)
print(Y.shape)

#thay chuoi bang so

categoroies = np.unique(Y) #Lay cac chuoi duy nhat trong mot mang numpy
for i in range(categoroies.size):
    Y = np_f.replace(Y, categoroies[i], str(i)) #replace de thay doi gia tri cua chuoi

#dua ve kieu float
Y = Y.astype('float')
print(Y)
