"""Simple Linear Regression.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 09_linear_regression.py
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



def linear_regression():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only feature 2 (BMI).
    X = diabetes_X[:, np.newaxis, 2]
    X_train, X_test = X[:-20], X[-20:]
    y_train, y_test = diabetes_y[:-20], diabetes_y[-20:]

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Simple Linear Regression (Diabetes BMI feature)")
    print("Coefficient:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R2 score:", r2_score(y_test, y_pred))

    order = np.argsort(X_test[:, 0])
    plt.scatter(X_test[:, 0], y_test, label="Actual")
    plt.plot(X_test[order, 0], y_pred[order], label="Regression line")
    plt.xlabel("BMI")
    plt.ylabel("Diabetes progression")
    plt.title("Simple Linear Regression")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    linear_regression()
