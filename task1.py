import numpy as np

x = np.array([[5,3,2], [54,33,7], [1,63,6]])
print(x)

x_min = x.min(1)
print(x_min)

x_max = x_min.max();
print(x_max)