# multiply two array of same size element by element

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = arr1 * arr2

print("Array 1:")
print(arr1)

print("Array 2:")
print(arr2)

print("Element-wise multiplication:")
print(result)