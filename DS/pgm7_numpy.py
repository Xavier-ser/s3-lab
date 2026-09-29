import numpy as np

# Create an array containing random integers
arr = np.random.randint(low=-10, high=40, size=10)

# Display the array
print(arr)

# Get a number from the user
num = int(input("Enter a number: "))

# Find positions where the number occurs
result = np.where(arr == num)

# If no position was found
if len(result[0]) == 0:
    print("Number is not present in the array")

# Otherwise the number exists
else:
    print("Number is present in the array")