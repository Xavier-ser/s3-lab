import matplotlib.pyplot as plt
import numpy as np

math_marks = np.array([
    88, 92, 80, 89, 100,
    80, 60, 100, 80, 34
])

science_marks = np.array([
    35, 79, 79, 48, 100,
    88, 32, 45, 20, 30
])

marks_range = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
])

# Plot Maths
plt.scatter(
    marks_range,
    math_marks,
    label="Maths"
)

# Plot Science
plt.scatter(
    marks_range,
    science_marks,
    label="Science"
)

plt.xlabel("Marks Range")
plt.title("Math marks vs Science marks")

plt.legend()
plt.show()