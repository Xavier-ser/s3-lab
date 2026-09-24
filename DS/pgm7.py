# numpy pgm to save given array to txt file and load it 

# np.savetxt is used to store your file
# np.loadtxt is used to load it in your pgm

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

np.savetxt("array.txt", arr, dtype=int)

print("Array saved to file")

new_arr = np.loadtxt("array.txt", dtype=int)  

print("New array")
print(new_arr) 




























