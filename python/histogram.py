import numpy as np
import matplotlib.pyplot as plt

# heights = np.array([
#     175,
#     165,
#     164,
#     164,
#     171,
#     165,
#     160,
#     169,
#     164,
#     159,
#     163,
#     167,
#     163,
#     172,
#     159,
#     160,
#     156,
#     162,
#     166,
#     162,
#     158,
#     167,
#     160,
#     161,
#     156,
#     172,
#     168,
#     165,
#     165,
#     177
# ])
# plt.hist(heights, bins = 6)
# plt.xlabel("height")
# plt.ylabel("frequency")
# plt.show()

# f1 = np.random.normal(loc = 0, scale = 1, size = 10000)
# f2 = np.random.normal(loc = 3, scale = .5, size = 10000)

# plt.hist(f1, bins = 200, color = "red", alpha = .7, label = "loc = 0, scale = 1")
# plt.hist(f2, bins = 200, color = "blue", alpha = .5, label = "loc = 3, scale = .5")
# plt.legend(loc = "best")
# plt.show()

from scipy.stats import norm

data = norm.rvs(10.0, 3, size = 1000)

plt.hist(data, bins = 20, density = True, alpha = 0.6, color = "b")

mu, std = norm.fit(data)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, "r", linewidth = 2)

plt.show()