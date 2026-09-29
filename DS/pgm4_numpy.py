import numpy as np

# Create an array
arr = np.array([12, 34, 6, 28, 46, 90, 3])

# Find the difference between neighbouring elements
diffs = np.diff(arr)

# Display original array
print("Array =", arr)

# Display differences
print("Difference =", diffs)