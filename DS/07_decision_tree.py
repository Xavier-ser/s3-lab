"""Decision Tree classification using Iris.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 07_decision_tree.py
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



def decision_tree():
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=78
    )

    model = DecisionTreeClassifier(random_state=78)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Decision Tree Classifier (Iris dataset)")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(metrics.classification_report(
        y_test, y_pred, target_names=iris.target_names
    ))

    sample = [[3, 4, 5, 6]]
    prediction = model.predict(sample)[0]
    print("Predicted class for", sample[0], ":", iris.target_names[prediction])

    tree.plot_tree(model, feature_names=iris.feature_names,
                   class_names=iris.target_names, filled=True)
    plt.title("Decision Tree")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    decision_tree()
