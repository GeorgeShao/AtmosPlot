import matplotlib.pyplot as plt
from main import DATA
import numpy as np

for i in range(len(DATA) // 2):
    #master_ozone.append()
    #master_acid.append()


    plt.scatter(list(range(1, 151)), DATA[i*2], color='blue') #ozone
    plt.scatter(list(range(1, 151)), DATA[(i*2)+1], color='red') #Hydrochloric acid

plt.xlabel('Elevation (km)')
plt.ylabel('Concentration (ppm)')
plt.show()