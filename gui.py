import matplotlib.pyplot as plt
import matplotlib
from main import DATA
import numpy as np

fig, ax1 = plt.subplots()
DATA_POINT_SPLIT = 3

ax2 = ax1.twinx()

for i in range(len(DATA) // DATA_POINT_SPLIT):
    coords = DATA[i*DATA_POINT_SPLIT+2]
    red_amount = (coords[0] + 90) / 180
    blue_amount = (coords[2] + 180) / 360
    # print(red_amount, blue_amount)
    ax1.scatter(list(range(1, 151)), DATA[i*DATA_POINT_SPLIT], facecolor=matplotlib.colors.to_hex((red_amount, 0, blue_amount),keep_alpha=False), s=1, marker=',')  # ozone
    ax2.scatter(list(range(1, 151)), DATA[(i*DATA_POINT_SPLIT)+1], facecolor=matplotlib.colors.to_hex((red_amount, 1, blue_amount),keep_alpha=False), s=1, marker=',')  # hydrochloric acid


ax1.set_xlabel('Elevation (km)')
ax1.set_ylabel('Concentration (ppm)')
ax2.set_ylabel('Concentration (ppm)')
ax1.set_ylim(ymin=0)
ax2.set_ylim(ymin=0)
plt.show()