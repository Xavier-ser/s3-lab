"""KNN classification using the diabetes dataset and a scatter plot.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 05_knn_diabetes.py
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



def knn_diabetes():
    db = datasets.load_diabetes()
    X, y = db.data, db.target

    # Standardize feature values before calculating KNN distances.
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Convert continuous target values into three categories.
    y_binned = np.digitize(y, bins=[y.mean() - y.std(), y.mean() + y.std()])

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_binned, train_size=0.7, random_state=42
    )

    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print("KNN on Diabetes dataset (target divided into 3 groups)")
    print("Accuracy:", accuracy_score(y_test, y_pred))

    df = pd.DataFrame(X, columns=db.feature_names)
    df["Outcome"] = y_binned
    plt.figure(figsize=(8, 5))
    plt.scatter(df["bmi"], df["bp"], c=df["Outcome"], alpha=0.7)
    plt.xlabel("BMI")
    plt.ylabel("Blood pressure (bp feature)")
    plt.title("Diabetes Dataset: BMI vs BP, coloured by target group")
    plt.colorbar(label="Target group")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    knn_diabetes()
