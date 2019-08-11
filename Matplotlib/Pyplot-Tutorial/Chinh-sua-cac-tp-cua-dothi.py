# import matplotlib.pyplot as plt

# days = list(range(1, 9))

# celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

# fig, ax = plt.subplots()

# ax.plot(days, celsius_values)
# ax.set_xlabel('Day')
# ax.set_ylabel('Degrees Celsius')

# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# X = np.linspace(-2*np.pi, 2*np.pi, 70, endpoint=True)
# F1 = np.sin(2*X)
# F2 = (2*X**5 + 4*X**4 - 4.8*X**3 + 1.2*X**2 + X + 1)*np.exp(-X**2)

# plt.plot(X, F2, '-r', linewidth=3)
# plt.plot(X, F1, '-b', linewidth=3)

# plt.show()


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2*np.pi, 2*np.pi, 70, endpoint=True)
F1 = X*np.sin(X)

ax = plt.gca()

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


xticks = np.arange(-np.pi*2, np.pi*2+1, np.pi)
replace_x_ticks = [r"$%d\pi$" % (i/np.pi) for i in xticks]

plt.xticks(xticks, replace_x_ticks)

for xtick in ax.get_xticklabels():
    xtick.set_fontsize(18)
    xtick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))


for ytick in ax.get_yticklabels():
    ytick.set_fontsize(14)
    ytick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))


plt.plot(X, F1, '--b', linewidth=3)
plt.legend(loc='lower left')

plt.show()
