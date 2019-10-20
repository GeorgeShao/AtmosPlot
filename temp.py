import numpy as np
import matplotlib.pyplot as plt
import time
# Fixing random state for reproducibility
np.random.seed(19680801)

start = time.time()
N = 10000
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=1, c=colors, alpha=0.5)
end = time.time()
print(end - start)
plt.show()