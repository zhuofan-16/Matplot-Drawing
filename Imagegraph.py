import matplotlib.pyplot as plt
import numpy as np
array=np.random.rand(3,3)*11
print(array)
plt.imshow(array,interpolation='nearest',cmap='bone',origin='upper')
plt.yticks(())
plt.xticks(())
plt.colorbar()
plt.show()
