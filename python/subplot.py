import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np

fig, ax = plt.subplots(2, 2)

x = np.random.randn(100)
y = np.random.randn(100)
ax[0, 0].scatter(x, y)

x = np.arange(10)
y = np.random.uniform(1, 10, 10)
ax[0, 1].bar(x, y)

x = np.linspace(0, 10, 100)
y = np.cos(x)
ax[1, 0].plot(x, y)

z = np.random.uniform(0, 1, (5, 5))
ax[1, 1].imshow(z)

plt.show()