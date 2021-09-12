import matplotlib.pyplot as plt
import numpy as np
plt.figure()
plt.subplot(2,2,1)
x=np.linspace(-10,10,50)
y=2*x+1
plt.plot(x,y,color='pink')
plt.subplot(2,2,2)
x=np.linspace(-2,2,50)
y=2*x+2
plt.plot(x,y,color='pink')
plt.subplot(2,2,3)
x=np.linspace(-2,2,50)
y=2*x**2+2
plt.plot(x,y,color='pink')
plt.subplot(2,2,4)
x=np.linspace(-2,2,50)
y=2*x**3+2
plt.plot(x,y,color='pink')

plt.show()