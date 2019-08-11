#Dua tren cac bai tap tren khoa hoc: aivietnam.ai/Week5 (https://aivietnam.ai/courses/aisummer2019/lessons/hoc-numpy-qua-vi-du/)

import numpy as np

# #Cau 2: tao mot mang boolen 2x3 voi tat ca gia tri la True

# #C1:
# arr1 = np.ones((2, 3)) > 0
# print(arr1)
# #C2
# arr1 = np.ones((2, 3), dtype=bool)
# print(arr1)
# #C3
# arr1 = np.full((2, 3), True, dtype=bool)
# print(arr1)


# #Cau 3: Lay nhung phan tu thoa man mot dieu kien cho truoc

# arr = np.arange(10)
# print(arr)

# #tim phan tu co gia tri le
# arr_odd = arr[arr % 2 == 1]
# print(arr_odd)
# #tim phan tu co gia tri chan
# arr_even = arr[arr % 2 == 0]
# print(arr_even)


# #Cau 4: Thay the phan tu thoa man mot dieu kien cho truoc bang mot gia tri khac
# #Mang ban dau gia tri bi thay doi

# arr = np.arange(10)
# print(arr)
# #Thay the phan tu co gia tri le bang 10
# arr[arr % 2 == 1] = 10
# print(arr)


# #Cau 5: Thay the phan tu thoa man mot dieu kien cho truoc bang mot gia tri khac
# #Mang ban dau gia tri ko bi thay doi

# arr = np.arange(10)
# print(arr)

# #thay the gia tri le bang 10 trong mot mang moi
# out = np.where(arr % 2 == 1, 10, arr)
# print(out)
# print(arr)


# #Cau 6: Chuyen mang 1 chieu thanh mang 2 chieu

# arr = np.arange(10)
# print(arr)

# #-1 co y nghia la so cot cua arr_2d duoc tinh tu dong
# arr_2D = arr.reshape(2, -1)
# print(arr_2D)


# #Cau 7: Xep chong 2 mang theo chieu doc

# arr1 = np.arange(10).reshape(2, -1)
# print(arr1)

# arr2 = np.arange(10, 0, -1).reshape(2, -1)
# print(arr2)

# #Cach 1:
# out = np.concatenate([arr1, arr2], axis=0)  #axis=0 : chon theo cot
# print(out)

# #Cach 2:
# out = np.vstack([arr1, arr2])
# print(out)

# #Cach 3:
# out = np.r_[arr1, arr2]
# print(out)


# #Cau 8: Xep chong 2 mang theo chieu ngang
# arr1 = np.arange(10).reshape(2, -1)
# arr2 = np.arange( 10, 0, -1).reshape(2, -1)

# print(arr1)
# print(arr2)

# #Cach 1:
# out = np.concatenate([arr1, arr2], axis=1)
# print(out)

# #Cach 2:
# out = np.hstack([arr1, arr2])
# print(out)

# #Cach 3:
# out = np.c_[arr1, arr2]
# print(out)


# #Cau 9: Tao mang moi duoc lap lai tu mot mang khac

# arr = np.array([1, 2, 3])
# print(arr)

# #tao mang moi, lap lai moi phan tu cua arr 2 lan
# out1 = np.repeat(arr, 2)
# print(out1)

# #tao mang moi lap lai mang arr 2 lan
# out2 = np.tile(arr, 2)
# print(out2)


# #Cau 10: Tao mang moi lay phan tu chung tu 2 mang da cho

# a[rr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 4, 5, 6, 7])
# print(arr1)
# print(arr2)

# out = np.intersect1d(arr1, arr2)
# print(out)


# #Cau 11: Tu 2 mang cho truoc xoa tat ca cac phan tu o mang arr1 co trong arr2

# arr1 = np.array([2, 3, 4, 5])
# arr2 = np.array([3, 5, 7, 9])
# print(arr1)
# print(arr2)

# out = np.setdiff1d(arr1, arr2)

# print(out)


# #Cau 12: Lay tat ca cac vi tri ma cac phan tu co gia tri giong nhau

# arr1 = np.array([3, 4, 5, 6, 7, 8])
# arr2 = np.array([3, 3, 6, 6, 7, 7])

# print(arr1)
# print(arr2)

# index = np.where(arr1 == arr2)
# print(index)
# print(index[0])


# #Cau 13: Tim tat ca vi tri va gia tri cac phan tu co gia tri trong pham vi cho truoc

# arr = np.array([1, 7, 3, 9, 4, 8])
# print(arr)

# #Cach 1:
# index1 = np.where((arr >= 4) & (arr <= 8))
# out1 = arr[index1]
# print(index1)
# print(out1)

# #Cach 2:
# index2 = np.where(np.logical_and(arr >= 4, arr <= 8))
# out2 = arr[index2]
# print(index2)
# print(out2)

# #Cach 3:
# out3 = arr[(arr >= 4) & (arr <= 8)]
# print(out3)


# #Cau 14: Cho 2 mang cung kich thuoc. so sanh 2 phan tu tuong ung va lay gia tri lon hon cho mang moi

# arr1 = np.array([4, 6, 2, 8, 6, 9])
# arr2 = np.array([1, 5, 4, 9, 8, 5])
# print(arr1)
# print(arr2)

# #Cach 1: Tao ham tim so lon hon trong 2 so
# def max_value(x, y):
#     if x >= y:
#         return x
#     else:
#         return y

# #dung numpy.vectorize de ap dung ham max_value
# #otypes la key kieu du lieu cho mang output
# pair_max = np.vectorize(max_value, otypes=[float])
# out1 = pair_max(arr1, arr2)
# print(out1)

# #Cach 2: sd ham maximum
# out2 = np.maximum(arr1, arr2)
# print(out2)

# #Cachs 3: sd ham where
# out3 = np.where(arr1 > arr2, arr1, arr2)
# print(out3)


# #Cau 15: Hoan doi 2 cot trong mang 2 chieu.

# arr = np.arange(12).reshape(4, 3)
# print(arr)

# #hoan doi cot 1 va cot 2
# out = arr[:, [1, 0, 2]]
# print(out)


# #Cau 16: Hoan doi 2 hang trong mang

# arr = np.arange(12).reshape(4, 3)
# print(arr)

# #Hoan doi hang 1 va 2
# out = arr[[1, 0, 2, 3], :]
# print(out)


# #Cau 17: Dao nguoc cac hang trong mang

# arr = np.arange(12).reshape(4, 3)
# print(arr)

# out = arr[::-1]
# print(out)


# #Cau 18: Dao nguoc cac cot trong mang

# arr = np.arange(12).reshape(4, 3)
# print(arr)

# out = arr[:, ::-1]
# print(out)


# #Cau 19: sinh ra mang 2x3 voi cac so ngau nhien trong trong khoang (1,9) kieu float

# arr1 = np.random.uniform(1, 9, size=(2, 3))
# print(arr1)


# #Cau 20: In mang 2 chieu kieu float chi voi 2 so sau dau phay

# rand_arr = np.random.random([2, 3])
# print(rand_arr)

# #Gioi han in 2 so sau dau phay(da lam tron)
# np.set_printoptions(precision=2)
# print(rand_arr)
