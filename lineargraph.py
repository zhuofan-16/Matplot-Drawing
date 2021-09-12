import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='Microsoft YaHei'
matplotlib.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.figure(num=1,figsize=(5,8))
x=np.linspace(-10,10,50)
y=2*x+1
plt.plot(x,y,label='y=2x+1',color='red')
plt.legend(loc='lower right', bbox_to_anchor=(1,0.15))
pointx=2
pointy=2*pointx+1
plt.scatter(pointx,pointy,s=50)
plt.plot([0,pointx],[pointy,pointy],'k--')
plt.plot([pointx,pointx],[pointy,0],'k--')
control=plt.gca()
control.spines['right'].set_color('none')
control.spines['top'].set_color('none')
control.xaxis.set_ticks_position('bottom')
control.yaxis.set_ticks_position('left')
control.spines['bottom'].set_position(('data',0))
control.spines['left'].set_position(('data',0))
plt.annotate('一个位置',xy=(pointx,pointy),xytext=(pointx+5,pointy+0.25),arrowprops=dict(arrowstyle='->' ,connectionstyle='arc3,rad=0.2'))
plt.text(-10.5,15,'我曾吹过清晨与你擦肩而过的微风，\n这算不算与你相拥？',fontsize=8)
plt.show()