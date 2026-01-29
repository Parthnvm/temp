#numpy

import numpy as np

# np.array([1, 2, 3, 4, 5])

a = np.array([1, 2, 3])

# print(a.dtype)

# d = np.float32(1.0)
# print(d.dtype)

# Agrregations 
sum = np.sum(a)
print(sum)

print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.std(a))
