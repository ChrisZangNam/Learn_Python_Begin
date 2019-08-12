#Cau 12: Tao cot moi trong do moi phan tru co gia tri = (pentallength + sepallength)/2

import numpy as np

iris_2d = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

# 3Rut cot pentallengtg x sepallength
sepallength = iris_2d[:, 0].astype('float')
petallength = iris_2d[:, 2].astype('float')
new_col = (petallength + sepallength) / 2

#Dinh dang cot moi cung so chieu voi iris_2d
print(new_col.shape)
new_col = new_col[:, np.newaxis]
print(new_col.shape)

#them cot moi vao iris_2d dung ham hstack
out = np.hstack([iris_2d, new_col])
print(out.shape)
