import matplotlib.pyplot as plt
from main import DATA

x_axis = []
for i in range(1,151):
    x_axis.append(i)

plt.plot(x_axis, x_axis)
plt.ylabel('Concentration (ppm)')
plt.show()