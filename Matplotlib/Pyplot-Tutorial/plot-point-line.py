import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4]) #mac dinh la chuoi gia tri cau y va tu dong tao gia tri x
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0,6,0,20])
plt.show()

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--')  #Ve ham y =t kieu duong red, kieu ---
plt.plot(t, t ** 2, 'bs')  #Ve y = t^2 duong blue, kieu square(o vuong)
plt.plot(t, t ** 3, 'g^')  #Vve y =t^3 duong green, kieu tam giac
plt.show()
