# Decision Tree classifier
from sklearn.tree import DecisionTreeClassifier

# Pandas
import pandas as pd

# Iris dataset
from sklearn.datasets import load_iris

# Split dataset
from sklearn.model_selection import train_test_split

# Evaluation metrics
from sklearn import metrics


# Load Iris dataset
iris = load_iris()

# Input features
x = iris.data

# Target classes
y = iris.target


# Split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3
)


# Create Decision Tree
clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=4,
    min_samples_leaf=2
)

# Train the model
clf = clf.fit(x_train, y_train)

# Predict test data
y_pred = clf.predict(x_test)

# Create classification report
report = metrics.classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

# Display report
print(report)