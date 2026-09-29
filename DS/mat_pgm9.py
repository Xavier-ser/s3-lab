import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
df = pd.read_csv("medal.csv", delimiter=":")

# Get country column
countries = df["Country"].to_numpy()

# Get gold medal column
medals = df["Gold_Medal"].to_numpy()

# Create pie chart
plt.pie(
    medals,
    labels=countries,
    autopct="%1.1f%%"
)

plt.show()