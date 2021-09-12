import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
matplotlib.rcParams['font.family']='Microsoft YaHei'
matplotlib.rcParams['font.sans-serif']=['Microsoft YaHei']
x=np.linspace(-1,1,5000)
y=np.abs(x)+np.sqrt(1-x**2)
y2=np.abs(x)-np.sqrt(1-x**2)
plt.figure(num=2,figsize=(13,10));
## plt.scatter for points ,plot*
line1,=plt.plot(x,y2,color='pink',linewidth=2.0,label='ZhuoFan')
line2,=plt.plot(x,y,color='pink',linewidth=2.0,linestyle='-',label="ZhuoFan")
# plt.xlim((-1,2))
plt.ylim((-1,1.5))
# plt.xlabel("I am x")
# plt.ylabel("I am Y")
# new_ticks=np.linspace(0,10,3)
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([0,100,200],
#             ['$really\ bad\ \alpha$',r'$bad\ \alpha$','normal芜湖'])
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.legend(loc='lower right')
x0=1
y0=1
plt.scatter(x0,y0,s=50,color='red')
## Z order to arrange order like css
plt.plot([x0,x0],[0,1],'k--',lw=2,color='red')
plt.plot([0,x0],[1,1],'k--',lw=2,color='red')
plt.annotate('一条线',xy=(1,1),xycoords='data',xytext=(+1.20,+1),fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))
plt.text(-0.9,0.75,'我曾吹过清晨与你擦肩而过的微风，\n这算不算与你相拥？',fontsize=18)
print(plt.xticks())
print(ax.get_xticklabels())
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(20)
    ##Use alpha=0.7 for transparent level ,can use for plot ,scatter and this
    label.set_bbox(dict(facecolor='white',edgecolor='pink'))
plt.show()
