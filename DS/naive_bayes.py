# Split dataset into training and testing data
from sklearn.model_selection import train_test_split

# Gaussian Naive Bayes classifier
from sklearn.naive_bayes import GaussianNB

# Evaluation metrics
from sklearn import metrics

# Load Iris dataset
from sklearn.datasets import load_iris


# Load dataset
iris = load_iris()

# Input features
x = iris.data

# Target classes
y = iris.target


# Split data
# 70% training and 30% testing
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3,
    random_state=40
)


# Create Naive Bayes model
gnb = GaussianNB()

# Train the model
gnb.fit(x_train, y_train)

# Predict test data
y_pred = gnb.predict(x_test)

# Calculate accuracy
acc = metrics.accuracy_score(
    y_test,
    y_pred
)

# Generate classification report
report = metrics.classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

# Display accuracy
print(acc)

# Display precision, recall and F1-score
print(report)