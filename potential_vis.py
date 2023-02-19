from functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import sys
from PyQt5 import QtWidgets, uic
import pyqtgraph as pg
from PyQt5.QtCore import pyqtSlot as slot
Design, _ = uic.loadUiType(r"pot_vis.ui")
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
def V(r, th):
    if r / rm <= x1:
        return V10(r, th)
    elif r / rm > x2:
        return V30(r, th)
    else:
        return V20(r, th)
def pot_vis(dim = '2D', R = None, Th = None):
    fig = plt.figure()
    if dim == '3D':
        def makeData():
            x = np.arange(3.5, 10, 0.1)
            y = np.arange(-1, 1, 0.05)
            xgrid, ygrid = np.meshgrid(x, y)
            zgrid = np.asarray([[float(V(r, th) * 8.065) for r in x] for th in y])
            return xgrid, ygrid, zgrid

        x, y, z = makeData()
        axes = plt.axes(projection='3d')
        axes.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
        axes.set_xlabel('R')
        axes.set_ylabel('Угол theta')
        axes.set_zlabel('V(R,th)')
    else:
        axes = plt.axes()
        if R == None:
            axes.plot(np.arange(0.8482049*rm, 10, 0.01), [V(r, Th) * 8.065 for r in np.arange(0.8482049*rm, 10, 0.01)])
        else:
            axes.plot(np.linspace(-1, 1, 181), [V(R, th) * 8.065 for th in np.linspace(-1, 1, 181)])
    # plt.show()

# pot_vis('2D', R = 4.3)
class Visualiser(QtWidgets.QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.r = 3.87
        self.th = 0
        self.R = np.linspace(3.4, 10, 100)
        self.Th = np.linspace(-1, 1, 181)
        self.r_graph.plot(np.arccos(self.Th) / np.pi * 180,\
                                                     [float(V(self.r, theta)) for theta in self.Th], pen=(31, 119, 180))
        self.r_spin.valueChanged.connect(self.r_plot)
        self.r_slider.valueChanged.connect(self.r_plot)
        self.theta_spin.valueChanged.connect(self.theta_plot)
        self.theta_slider.valueChanged.connect(self.theta_plot)
    @slot()
    def r_plot(self):
        obj = self.sender().objectName()    # what has been triggered
        if obj[-4:] == 'spin':  # if spinbox's value changed
            self.r = self.r_spin.value()
            self.r_slider.setValue(int(self.r * 1_000))
        else:
            self.r = self.r_slider.value() / 1_000
            self.r_spin.setValue(self.r)
        self.r_graph.clear()
        self.r_graph.plot(np.arccos(self.Th) / np.pi * 180, [float(V(self.r, theta)) * 8.065 for theta in self.Th],\
                                                                                                    pen=(31, 119, 180))
    def theta_plot(self):
        obj = self.sender().objectName()  # what has been triggered
        if obj[-4:] == 'spin':  # if spinbox's value changed
            self.theta = self.theta_spin.value()
            self.theta_slider.setValue(int(self.theta * 10))
        else:
            self.theta = self.theta_slider.value() / 10
            self.theta_spin.setValue(self.theta)
        self.theta_graph.clear()
        self.theta_graph.plot(self.R, [float(V(r, np.cos(self.theta * np.pi / 180))) * 8.065\
                                                                                for r in self.R], pen=(31, 119, 180))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    app.setPalette(QtWidgets.QApplication.style().standardPalette())
    window = Visualiser()
    window.show()
    app.exec_()