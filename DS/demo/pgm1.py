# create two arrays using numpy and perform element wise comparison


import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([10, 25, 30, 35, 50])

print(np.equal(a, b))
print(np.not_equal(a, b))
print(np.greater(a, b))
print(np.less(a, b))
print(np.greater_equal(a, b))
print(np.less_equal(a, b))