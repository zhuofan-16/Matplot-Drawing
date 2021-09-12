import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['font.family']='Microsoft YaHei'
matplotlib.rcParams['font.sans-serif']=['Microsoft YaHei']

def func(x,y):
    #Find height using x and y
    # return 2*x
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)
## The 8 is divide by how many pieces ,if 8 means there is 10 pirce
plt.contourf(X,Y,func(X,Y),8,alpha=0.7,cmap=plt.cm.hot)
c=plt.contour(X,Y,func(X,Y),8,colors='black',linewidths=1.5)
plt.clabel(c,inline=True,fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()