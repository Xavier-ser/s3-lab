"""K-Means clustering with generated sample data.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 08_kmeans_clustering.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, tree
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score



def kmeans_clustering():
    data, _ = make_blobs(n_samples=300, centers=3, random_state=42)

    model = KMeans(n_clusters=3, random_state=42, n_init="auto")
    model.fit(data)

    labels = model.labels_
    centroids = model.cluster_centers_

    print("K-Means Clustering")
    print("Cluster labels:", np.unique(labels))
    print("Centroids:\n", centroids)
    print("Predicted clusters for [[2,-4], [6,6], [6,-2]]:")
    print(model.predict([[2, -4], [6, 6], [6, -2]]))

    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", s=200)
    plt.title("K-Means Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()


if __name__ == "__main__":
    kmeans_clustering()
