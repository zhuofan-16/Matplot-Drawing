import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
# ##Method 1 :Subplot2grid
# plt.figure()
# ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# x=np.linspace(-1,1,50)
# y=2*x+1
# ax1.plot(x,y)
# plt.title("y=2x+1")
# ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
# x1=np.linspace(-2,2,50)
# y1=2*x**3+2
# y2=2*x**2+2
#
# ax3=plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
# ax3.plot(x1,y2)
# ax3.set_title("y=2x^3+2",y=-0.2)
# ax4=plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
# ax5=plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)

# Method 2:Gridspec
plt.figure()
gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:2])
ax3=plt.subplot(gs[1:,2])
ax4=plt.subplot(gs[2,0])
ax5=plt.subplot(gs[2,1])


plt.tight_layout()
plt.show()