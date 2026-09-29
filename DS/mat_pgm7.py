import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(1, 6) * 3

y1 = np.array([22, 30, 35, 35, 26])
y2 = np.array([25, 22, 30, 35, 29])

bar_width = 0.4

# Bars for men
plt.bar(
    x_data - bar_width,
    y1,
    width=bar_width,
    label="Men"
)

# Bars for women
plt.bar(
    x_data + bar_width,
    y2,
    width=bar_width,
    label="Women"
)

plt.legend()
plt.title("Scores by person")

plt.show()