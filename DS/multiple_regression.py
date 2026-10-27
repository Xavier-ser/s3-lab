import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# Load Diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(
    return_X_y=True
)


# Select two features
# Feature 0 = Age
# Feature 2 = BMI
diabetes_X = diabetes_X[:, [0, 2]]


# Training data
diabetes_X_train = diabetes_X[:-20]
diabetes_y_train = diabetes_y[:-20]


# Testing data
diabetes_X_test = diabetes_X[-20:]
diabetes_y_test = diabetes_y[-20:]


# Create Multiple Linear Regression model
regr = linear_model.LinearRegression()


# Train the model
regr.fit(
    diabetes_X_train,
    diabetes_y_train
)


# Predict test data
diabetes_y_pred = regr.predict(
    diabetes_X_test
)


# Display coefficients
print("Coefficients:", regr.coef_)

# Display intercept
print("Intercept:", regr.intercept_)

# Calculate MSE
print(
    "Mean squared error:",
    mean_squared_error(
        diabetes_y_test,
        diabetes_y_pred
    )
)

# Calculate R²
print(
    "R^2 score:",
    r2_score(
        diabetes_y_test,
        diabetes_y_pred
    )
)