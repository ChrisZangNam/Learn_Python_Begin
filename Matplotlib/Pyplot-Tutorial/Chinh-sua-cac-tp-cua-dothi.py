import matplotlib.pyplot as plt

days = list(range(1, 9))

celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

fig, ax = plt.subplots()

ax.plot(days, celsius_values)
ax.set_xlabel('Day')
ax.set_ylabel('Degrees Celsius')

plt.show()
