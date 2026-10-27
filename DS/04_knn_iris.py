"""K-Nearest Neighbors classification using the Iris dataset.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 04_knn_iris.py
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



def knn_iris():
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=78
    )

    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print("KNN Classifier (Iris dataset)")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Actual labels:   ", y_test)
    print("Predicted labels:", y_pred)

    sample = [[3, 5, 4, 2]]
    prediction = classifier.predict(sample)[0]
    print("New sample:", sample[0])
    print("Predicted flower:", iris.target_names[prediction])


if __name__ == "__main__":
    knn_iris()
