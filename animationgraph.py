import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
from matplotlib import animation
figure=plt.figure()
ax=host_subplot(111)
x=np.arange(0,5*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
def animationfun(i):
    line.set_ydata(np.sin(x+i/10))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani=animation.FuncAnimation(fig=figure,func=animationfun,init_func=init,interval=100,blit=False,frames=120)
plt.show()