#Cau 17: Tim vi tri xuat hien dau tien cua mot gia tri nho hon 1.0 trong cot thu 4(petalwidth)

import numpy as np

iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')
print(iris[:14])

#Lay cot thu 4 petalwidth va dinh dang kieu float thoa man > 1.0
petalwidth = iris[:,3].astype('float')>1.0

#ham argwhre lay index cua mang thoa man dieu kien cho truoc
index = np.argwhere(petalwidth)[0]
print(index)
