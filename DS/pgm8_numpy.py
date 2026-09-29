import numpy as np

# Create an array
arr = np.array([4, 5, 4, 6, 11, 2235, 56])

# Save the array into a text file
np.savetxt("test.txt", arr)

print("Writing the array to the file")

# Read the array back from the file
data = np.loadtxt("test.txt")

# Display the loaded data
print("File content is:")
print(data)