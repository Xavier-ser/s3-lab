#numpy pgm to create matrix and to compute sum of all elements, sum of each column and sum of each row

import numpy as np

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

arr1 = np.arange(9)
arr = arr1.reshape(3,3)

print("Matrix:")
print(arr)

print("Sum of all elements:", np.sum(arr))
print("Sum of each column:", np.sum(arr, axis=0))
print("Sum of each row:", np.sum(arr, axis=1))

