#Chuan hoa(normalize) cot sepallength de giai tri nam trong khoang(0;1)

import numpy as np

#Trich xuat cot 1 tu iris thanh mang mot chieu
sepallength = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0])

#Cach 1: cong thuc chuan hoa 1 mang co gia tri tu 0-1
#norm_array_a = a(i) - min.a/(max.a - min.a)
norm_sepallength = (sepallength - sepallength.min()) / (sepallength.max() - sepallength.min())
#in 5 gia tri dau tien
print(norm_sepallength[:5])

#Cach 2: dung ham ptp() lay pham vi gia tri tuc (max-min)
norm_sepallength = (sepallength - sepallength.min()) / sepallength.ptp()
print(norm_sepallength[:5])
