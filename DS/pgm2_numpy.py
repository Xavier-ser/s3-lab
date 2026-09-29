import numpy as np

# Create a NumPy array
arr = np.array([23, 55, 29, 56, 28, 86, 12])

# Calculate the mean (average)
mean = np.mean(arr)

# Calculate variance
variance = np.var(arr)

# Calculate standard deviation
std = np.std(arr)

# Display the array
print("Array =", arr)

# Display calculated values
print("Mean =", mean)
print("Variance =", variance)
print("Standard deviation =", std)