from functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


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
    plt.show()

pot_vis('2D', R = 4.3)