#Cau 11: Chuye doi 3 cot pentallength thanh mang:
# Nho hon 3->small
# 3-5 ->medium
# >5 -> large

import numpy as np

iris = np.genfromtxt('iris.csv', delimiter=',', dtype='object')

#ham np.digitize: tra ve chi so cua bin ma moi phan tu thuoc khoang bin tuong ung
#chuyen doi mang sang mang bin tuong ung voi bang dinh nghia chuyen doi

bin_petallength = np.digitize(iris[:, 2].astype(float), [0, 3, 5, 10])  #chia thang 3 khoang 0-3, 3-5, 5-10

#anh xa bang bin thanh van ban tuong ung
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
map_bin_pentallength = [label_map[x] for x in bin_petallength]

print(map_bin_pentallength[:4])
