import numpy as np

# Create an array of complex numbers
arr = np.array([
    complex(7, 5),
    complex(4, 3),
    complex(12, 2),
    complex(1, 8),
    complex(1, 9)
])

# Sort the complex-number array
sorted_arr = np.sort(arr)

# Display original array
print("Array before sorting =", arr)

# Display sorted array
print("After sorting =", sorted_arr)