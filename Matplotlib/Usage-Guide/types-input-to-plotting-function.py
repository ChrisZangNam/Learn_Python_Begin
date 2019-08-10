#Do tat ca ca ham deu duoi dang np.array or np.ma.masked dau vao.
#Ta su dung thu vien pandas  va np.matrix de chuyen input sang dang np.array

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#use pd.DataFrame
a = pd.DataFrame(np.random.rand(4, 5), columns=list('abcde'))
a_asarray = a.values
print('Original data: \n')
print(a)
print('\nData after convert to array: \n')
print(a_asarray)

#use np.matrix

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
print('\nMatrix b : ')
print(b)
print('Array from matrix b is: ')
print(b_asarray)
