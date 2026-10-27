import matplotlib.pyplot as plt
import numpy as np

# Import datasets and Linear Regression
from sklearn import datasets, linear_model

# Import evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score


# Load Diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(
    return_X_y=True
)


# Select BMI feature
diabetes_X = diabetes_X[:, np.newaxis, 2]


# First part = training data
diabetes_X_train = diabetes_X[:-20]
diabetes_y_train = diabetes_y[:-20]


# Last 20 = testing data
diabetes_X_test = diabetes_X[-20:]
diabetes_y_test = diabetes_y[-20:]


# Create Linear Regression model
regr = linear_model.LinearRegression()


# Train model
regr.fit(
    diabetes_X_train,
    diabetes_y_train
)


# Predict test values
diabetes_y_pred = regr.predict(
    diabetes_X_test
)


# Display coefficient
print("Coefficients:", regr.coef_)

# Display intercept
print("Intercept:", regr.intercept_)

# Calculate Mean Squared Error
print(
    "Mean squared error:",
    mean_squared_error(
        diabetes_y_test,
        diabetes_y_pred
    )
)

# Calculate R² score
print(
    "R^2 score:",
    r2_score(
        diabetes_y_test,
        diabetes_y_pred
    )
)