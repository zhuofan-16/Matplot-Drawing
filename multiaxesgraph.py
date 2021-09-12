import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
fig=plt.figure()
x=[0,1,2,3,4,5]
y=[0,2,3,4,5,8]
y1=[-2,-4,-3,-5,5,6]
ax1=host_subplot(111)
##Mirror reverse
ax2=ax1.twinx()
line1=ax1.plot(x,y,'pink',label='Pink Line')
line2=ax2.plot(x,y1,'skyblue',label='Blue Line')
ax1.set_ylabel("Pink Line")
ax2.set_ylabel('Blue Line')
#If never import from mpl_toolkits.axes_grid1 import host_subplot
# line=line1+line2
# lines=[l.get_label() for l in line]
# print(lines)
# print(ax2.yaxis.get_label(),ax1.yaxis.get_label())
# plt.legend(line,lines)
legend=plt.legend()
legend.texts[0].set_color('pink')
legend.texts[1].set_color('skyblue')


plt.show()