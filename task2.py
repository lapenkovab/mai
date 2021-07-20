import numpy as np
# import numpy.random as rand

x = np.random.randint(0, 100, 10)
print(x)

x[x > 10] = -1


print(x)
