'''
numpy.arange: Tra ve mang cac gai tri cach deu nhau

cu phap:
        numpy.arange(start, stop, step, dtype)
'''

import numpy as np

x = np.arange(5)
print(x)

x = np.arange(10, 20, 2)
print(x)

'''
numpy.linspace: Tuong tu arange. Thay vi step, se chi dinh so luong cac so trong array ma ra step tuong ung.

Cu phap:
        numpy.linspace(start, stop, num, endpoint, retstep, dtype)
'''
x = np.linspace(10, 20, 5)  #tu 10, 20 gom 5 so dan cach deu
print(x)

x = np.linspace(10, 20, 5, endpoint=False) #Ko tinh can cuoi
print(x)

x = np.linspace(1, 2, 5, retstep=True) #in ra step
print(x)

'''
numpy.logspace: tra ve mang cac so cach deu nhau tren thang do log

Cu phap:
        numpy.logspace(start, stop, num, endpoint, base, dtype)
'''
x = np.logspace(1.0, 2.0, num=10)
print(x)
x = np.logspace(1, 10, num=10, base=2) #array 2^x
print(x)
