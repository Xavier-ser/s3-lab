# write numpy pgm to display all the even integers from 50 to 90

import numpy as np

arr = np.arange(50, 91)

print(arr[arr % 2 == 0])