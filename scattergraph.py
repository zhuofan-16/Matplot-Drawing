import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
matplotlib.rcParams['font.family']='Microsoft YaHei'
matplotlib.rcParams['font.sans-serif']=['Microsoft YaHei']

n=1024
##np.random.normal --0 for average value ,1 for standard deriv,n for number of values)
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
plt.title('我曾吹过清晨与你擦肩而过的微风,这算不算与你相拥？\n 散点图')
T=np.arctan2(Y,X) # for color value
plt.scatter(X,Y,s=75,c=T)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.show()