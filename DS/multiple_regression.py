# PROGRAM 10: MULTIPLE REGRESSION

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the Diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Select features 0 and 2
diabetes_X = diabetes_X[:, [0, 2]]

# Split the input data into training and testing data
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the output data into training and testing data
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# Create the Multiple Regression model
regr = linear_model.LinearRegression()

# Train the model
regr.fit(diabetes_X_train, diabetes_y_train)

# Predict the output using testing data
diabetes_y_pred = regr.predict(diabetes_X_test)

# Display model results
print("Coefficients:", regr.coef_)
print("Intercept:", regr.intercept_)

print(
    "Mean squared error: %.2f"
    % mean_squared_error(diabetes_y_test, diabetes_y_pred)
)

print(
    "R^2 score: %.2f"
    % r2_score(diabetes_y_test, diabetes_y_pred)
)

# Create the figure
plt.figure(figsize=(14, 5))

# First graph: Feature 0 (Age)
plt.subplot(1, 2, 1)

plt.scatter(
    diabetes_X_test[:, 0],
    diabetes_y_test,
    color='red',
    marker='o',
    label='Actual',
    alpha=0.7
)

plt.scatter(
    diabetes_X_test[:, 0],
    diabetes_y_pred,
    color='blue',
    marker='^',
    label='Predicted',
    alpha=0.7
)

plt.xlabel('Feature 0 (Age)')
plt.ylabel('Diabetes Progression')
plt.title('Feature 0 vs Target')
plt.legend()

# Second graph: Feature 2 (BMI)
plt.subplot(1, 2, 2)

plt.scatter(
    diabetes_X_test[:, 1],
    diabetes_y_test,
    color='red',
    marker='s',
    label='Actual',
    alpha=0.7
)

plt.scatter(
    diabetes_X_test[:, 1],
    diabetes_y_pred,
    color='green',
    marker='D',
    label='Predicted',
    alpha=0.7
)

plt.xlabel('Feature 2 (BMI)')
plt.ylabel('Diabetes Progression')
plt.title('Feature 2 vs Target')
plt.legend()

# Adjust graph spacing
plt.tight_layout()

# Display the graphs
plt.show()








# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# # Manually create input data: Age and BMI
# diabetes_X = np.array([
#     [25, 20],
#     [30, 22],
#     [35, 25],
#     [40, 27],
#     [45, 28],
#     [50, 30],
#     [55, 32],
#     [60, 35]
# ])

# # Manually create target data: Diabetes progression
# diabetes_y = np.array([80, 100, 120, 140, 160, 180, 200, 220])

# # Split data into training and testing sets
# diabetes_X_train = diabetes_X[:-2]
# diabetes_X_test = diabetes_X[-2:]

# diabetes_y_train = diabetes_y[:-2]
# diabetes_y_test = diabetes_y[-2:]

# # Create and train the model
# regr = LinearRegression()
# regr.fit(diabetes_X_train, diabetes_y_train)

# # Predict values
# diabetes_y_pred = regr.predict(diabetes_X_test)

# # Display results
# print("Coefficients:", regr.coef_)
# print("Intercept:", regr.intercept_)
# print("Mean Squared Error:", mean_squared_error(diabetes_y_test, diabetes_y_pred))
# print("R2 Score:", r2_score(diabetes_y_test, diabetes_y_pred))

# # Plot actual and predicted values
# plt.scatter(diabetes_X_test[:, 0], diabetes_y_test, color="red", label="Actual")
# plt.scatter(diabetes_X_test[:, 0], diabetes_y_pred, color="blue", label="Predicted")

# plt.xlabel("Age")
# plt.ylabel("Diabetes Progression")
# plt.title("Multiple Linear Regression")
# plt.legend()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# # Step 1: Read the CSV dataset
# data = pd.read_csv("diabetes.csv")

# # Step 2: Select input features and target
# X = data[["Age", "BMI"]]
# y = data["Progression"]

# # Step 3: Split into training and testing data
# X_train = X.iloc[:-2]
# X_test = X.iloc[-2:]

# y_train = y.iloc[:-2]
# y_test = y.iloc[-2:]

# # Step 4: Create the model
# model = LinearRegression()

# # Step 5: Train the model
# model.fit(X_train, y_train)

# # Step 6: Predict the target values
# y_pred = model.predict(X_test)

# # Step 7: Display results
# print("Coefficients:", model.coef_)
# print("Intercept:", model.intercept_)
# print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))

# # Step 8: Plot actual and predicted values
# plt.scatter(X_test["Age"], y_test, color="red", label="Actual")
# plt.scatter(X_test["Age"], y_pred, color="blue", label="Predicted")

# plt.xlabel("Age")
# plt.ylabel("Progression")
# plt.title("Multiple Linear Regression")
# plt.legend()
# plt.show()