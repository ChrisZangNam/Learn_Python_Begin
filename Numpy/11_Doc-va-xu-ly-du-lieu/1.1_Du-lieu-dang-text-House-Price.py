'''
Du lieu dang text thuong duoc luu trong file .csv.
Moi du lieu duoc luu thanh mot dong va cac truong cach nhau = dau phay.
'''

#Doc file Boston.csv

import numpy as np

data = np.genfromtxt('Boston.csv', dtype='float', delimiter=',', skip_header=1)
#skip_header=1 de bo dong dau tien, dtype='float' do kieu du lieu trong file chua so float.
print(data.shape)

X = data[:, :-1]
Y = data[:, -1]

print(X.shape)
print(Y.shape)
