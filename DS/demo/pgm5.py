# write numpy pgm to create 5x5 0 matrix, diagonal elements 1 2 3 4 5 

import numpy as np

arr = np.zeros((5,5), dtype=int)

arr[np.diag_indices(5)] = [1,2,3,4,5]

print(arr)