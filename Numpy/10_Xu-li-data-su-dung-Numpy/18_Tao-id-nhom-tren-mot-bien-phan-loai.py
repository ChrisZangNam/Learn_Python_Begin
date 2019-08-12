#Cau 18: Tao id nhom dua tren mot bien phan loai cho truoc, sung cot species tu mang iris

import numpy as np

species = np.genfromtxt('iris.csv', delimiter=',', dtype='object', usecols=4)

#Cach 1:
output = [np.argwhere(np.unique(species)==s).tolist()[0][0]
          for val in np.unique(species)
          for s in species[species==val]]
print(output)

#Cach 2: dung vong lap
output =[]
uniqs = np.unique(species)

#Lap nhung gia tri duy nhat
for val in uniqs:
    #tim moi phan tu trong mang
    for s in species[species==val]:
        groupid = np.argwhere(uniqs==s).tolist()[0][0]

        #chen vao mang ket qua
        output.append(groupid)

print(output)