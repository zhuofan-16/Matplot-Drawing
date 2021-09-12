import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
x=[0,1,2,3,4,5]
y=[0,2,3,4,5,6]
y=[-2,-4,-3,-5,5,6]
left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
plt.plot(x,y)
ax2=fig.add_axes([0.15,0.55,0.3,0.3])
ax2.plot(y,x)
ax3=fig.add_axes([0.55,0.2,0.3,0.3])
ax3.plot(x,y)

plt.show()