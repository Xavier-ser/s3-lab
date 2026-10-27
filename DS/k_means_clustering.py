# Scikit-learn datasets
from sklearn import datasets

# Plotting
import matplotlib.pyplot as plt

# K-Means algorithm
from sklearn.cluster import KMeans


# Load Iris dataset
iris = datasets.load_iris()

# Use only first two features
X = iris.data[:, :2]

# Actual class labels
y = iris.target


# Create K-Means model
# Number of clusters = 3
kmeans = KMeans(
    n_clusters=3,
    random_state=21
)

# Train K-Means
kmeans.fit(X)

# Get predicted cluster labels
labels = kmeans.labels_


# Display actual classes
plt.subplot(1, 2, 1)

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y
)

plt.title("Actual")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")


# Display predicted clusters
plt.subplot(1, 2, 2)

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels
)

plt.title("Predicted")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.tight_layout()
plt.show()






from sklearn.metrics import (
    adjusted_rand_score,
    normalized_mutual_info_score
)

# Calculate ARI
ari = adjusted_rand_score(y, labels)

# Calculate NMI
nmi = normalized_mutual_info_score(y, labels)

print("Adjusted Rand Index (ARI):", ari)
print("Normalized Mutual Information (NMI):", nmi)