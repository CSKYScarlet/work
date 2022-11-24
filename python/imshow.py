import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((10, 10))
plt.imshow(data)
plt.colorbar()

plt.show()