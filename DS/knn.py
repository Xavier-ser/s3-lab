# Load the Iris dataset
from sklearn.datasets import load_iris

# Function for splitting data into training and testing
from sklearn.model_selection import train_test_split

# KNN classifier
from sklearn.neighbors import KNeighborsClassifier

# Evaluation metrics
from sklearn import metrics

# Load Iris dataset
iris = load_iris()

# Input features
x = iris.data

# Target/class labels
y = iris.target

# Split dataset
# 75% training, 25% testing
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25
)

# Create KNN model
# k = 5
model = KNeighborsClassifier(n_neighbors=5)

# Train the model
model.fit(x_train, y_train)

# Predict classes for test data
y_prediction = model.predict(x_test)

# Calculate accuracy
accuracy = metrics.accuracy_score(
    y_test,
    y_prediction
)

print("Accuracy =", accuracy)

# Create a new sample
sample = [[2, 2, 2, 2]]

# Predict its class
pred = model.predict(sample)[0]

# Display flower name
print(
    "New Sample belongs to",
    iris.target_names[pred]
)