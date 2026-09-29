import matplotlib.pyplot as plt
import numpy as np

# Open the text file
file = open("exercise3.3.txt")

# Read first line and convert values into integers
x_data = np.array(
    list(map(int, file.readline().strip().split(",")))
)

# Read second line
y_data = np.array(
    list(map(int, file.readline().strip().split(",")))
)

# Close the file
file.close()

# Add title
plt.title("Temperature Information")

# Label axes
plt.xlabel("Day")
plt.ylabel("Temperature")

# Plot the data
plt.plot(
    x_data,
    y_data,
    ls="-",
    marker="*"
)

plt.show()