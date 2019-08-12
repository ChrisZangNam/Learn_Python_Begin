#Cau 6: tinh softmax cho cot sepallength

import numpy as np

sepallength = np.genfromtxt('iris.csv', delimiter=',', dtype=float, usecols=[0])

def softmax(x):
    #tinh gia tri softmax cho tung phan tu cua x
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

#in chi 3 so le
np.set_printoptions(precision=4)
print(softmax(sepallength))
