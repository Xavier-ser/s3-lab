import numpy as np

# Create a NumPy array containing Fahrenheit temperatures
fht = np.array([100, 98.4, 91.50, 99.78, 101.5])

# Create an empty NumPy array to store Celsius values
degree = np.array([])

# Take each temperature from the Fahrenheit array
for temp in fht:

    # Convert Fahrenheit to Celsius
    degreeval = (temp - 32) * (5 / 9)

    # Add the Celsius value to the degree array
    degree = np.append(degree, degreeval)

# Display Fahrenheit values
print("Fahrenheit values:", fht)

# Display converted Celsius values
print("Centigrade values:", degree)