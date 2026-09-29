import numpy as np

# Generate 10 random integers from -40 to 39
arr = np.random.randint(low=-40, high=40, size=10)

# Display the array
print("Array =", arr)

# Find elements greater than 4
result = arr[arr > 4]

# Display the result
print("Elements greater than 4 =", result)