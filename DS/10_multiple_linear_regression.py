"""Multiple Linear Regression.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 10_multiple_linear_regression.py
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



def multiple_linear_regression():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Feature 0 is age; feature 2 is BMI.
    X = diabetes_X[:, [0, 2]]
    X_train, X_test = X[:-20], X[-20:]
    y_train, y_test = diabetes_y[:-20], diabetes_y[-20:]

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Multiple Linear Regression (Age and BMI)")
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R2 score:", r2_score(y_test, y_pred))

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(X_test[:, 0], y_test, label="Actual")
    plt.scatter(X_test[:, 0], y_pred, marker="^", label="Predicted")
    plt.xlabel("Age feature")
    plt.ylabel("Diabetes progression")
    plt.title("Age vs Target")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(X_test[:, 1], y_test, label="Actual")
    plt.scatter(X_test[:, 1], y_pred, marker="^", label="Predicted")
    plt.xlabel("BMI feature")
    plt.ylabel("Diabetes progression")
    plt.title("BMI vs Target")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    multiple_linear_regression()
