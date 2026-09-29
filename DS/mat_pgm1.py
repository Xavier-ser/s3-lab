import matplotlib.pyplot as plt
import numpy as np

# X-axis values
x_data = np.array([1, 2, 6, 18])

# Y-axis values
y_data = np.array([3, 10, 12, 20])

# Draw the line
plt.plot(
    x_data,
    y_data,
    ls=":",          # dotted line
    marker=".",      # point marker
    ms=10,           # marker size
    mfc="green",     # marker face colour
    mec="green",     # marker edge colour
    color="red"      # line colour
)

# Display graph
plt.show()