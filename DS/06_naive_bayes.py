"""Gaussian Naive Bayes classification using Iris.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 06_naive_bayes.py
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



def naive_bayes():
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=40
    )

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Naive Bayes Classifier (Iris dataset)")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(metrics.classification_report(
        y_test, y_pred, target_names=iris.target_names
    ))


if __name__ == "__main__":
    naive_bayes()
