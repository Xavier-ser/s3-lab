import numpy as np

# Create a 3 × 3 matrix
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Array =", arr)

# Sum of every element
total_sum = np.sum(arr)
print("Sum of elements =", total_sum)

# Sum of each column
col_sum = np.sum(arr, axis=0)
print("Column wise sum =", col_sum)

# Sum of each row
row_sum = np.sum(arr, axis=1)
print("Row wise sum =", row_sum)