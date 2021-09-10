import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='Microsoft YaHei'
matplotlib.rcParams['font.sans-serif']=['Microsoft YaHei']

n=12
## Create a 12 space array
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1,n)
plt.bar(X,Y1,color='skyblue',edgecolor='white')
plt.bar(X,-Y2,color='pink',edgecolor='white')
plt.xticks(())
plt.yticks(())
control=plt.gca()
control.spines['left'].set_color('none')
control.spines['top'].set_color('none')
control.spines['right'].set_color('none')
control.spines['bottom'].set_color('none')
for x,y in zip(X,Y1):
    # ha: horizontal alignment,choose center
    plt.text(x,y+0.1,'%.1f'%y,ha='center')

for x,y in zip(X,-Y2):
    plt.text(x,y-0.1,'%.1f'%y,ha='center')

plt.show()
