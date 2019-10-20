import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
from main import DATA
import numpy as np
from PyQt5 import QtCore, QtWidgets

fig, ax1 = plt.subplots()
DATA_POINT_SPLIT = 3

ax2 = ax1.twinx()

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

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