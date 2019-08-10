import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  #init 100 element in [0,2]
# print(x)

plt.plot(x, x, label='linear')  #plot function y=x
plt.plot(x, x ** 2, label='qudratic')  #plot function y = x^2
plt.plot(x, x ** 3, label='cubic')  #plot function y = x^3

plt.xlabel('x lebel')  #title of axis x
plt.ylabel('y label')  #title of axis y

plt.title('Simple Plot')

plt.legend()  #comment for line

plt.show()
