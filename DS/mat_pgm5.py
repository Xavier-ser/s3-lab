import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])

# Highest temperatures
y1 = np.array([30, 32, 31, 32, 33])

# Lowest temperatures
y2 = np.array([27, 26, 29, 28, 29])

plt.xlabel("Day")

# Plot first line
plt.plot(
    x, y1,
    marker=".",
    label="Highest Temperature"
)

# Plot second line
plt.plot(
    x, y2,
    marker=".",
    label="Lowest Temperature"
)

plt.title("Temperature Difference")

# Display labels for both lines
plt.legend()

plt.show()