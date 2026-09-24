# create 4x4 array with random values. create a new array from the said array by swapping first and last rows

import numpy as np

arr = np.random.randint(1, 10, (4, 4))

print("Original array:")
print(arr)

new_arr = arr[[3, 1, 2, 0]]

print("After swapping first and last rows:")
print(new_arr)