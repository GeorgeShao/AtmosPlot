import matplotlib.pyplot as plt
from main import DATA
import numpy as np

fig, ax1 = plt.subplots()

for i in range(len(DATA) // 2):
    #master_ozone.append()
    #master_acid.append()

    ax1.scatter(list(range(1, 151)), DATA[i*2], color='blue', s=1) #ozone
    ax2 = ax1.twinx()
    ax2.scatter(list(range(1, 151)), DATA[(i*2)+1], color='red', s=1) #Hydrochloric acid


ax1.set_xlabel('Elevation (km)')
ax1.set_ylabel('Concentration (ppm)')
ax2.set_ylabel('Concentration (ppm)')
plt.show()