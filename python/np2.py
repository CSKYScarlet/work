import numpy as np

n = 1000
sum = 0
arr = np.random.rand(n, n)
for i in range(n):
    for j in range(n):
        sum += arr[i][j]
print(sum)