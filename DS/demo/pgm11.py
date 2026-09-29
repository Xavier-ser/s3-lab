# # python pgm to predict diabetes using KNN alg

# from sklearn.datasets import load_diabetes

# diabetes = load_diabetes()

# print(diabetes.data[:5])
# print(diabetes.target)

# print(len(diabetes.data))
# print(diabetes.data.shape)
# print(diabetes.target.shape)

# print(diabetes.feature_names)
# print(len(diabetes.feature_names))

# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, r2_score
# from sklearn.datasets import load_diabetes

# data = load_diabetes()

# X = data.data
# y = (data.target > 140).astype(int)

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# model = KNeighborsClassifier(n_neighbors=5)

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))

# print("Confusion Matrix:")
# print(confusion_matrix(y_test, y_pred))

# print("Classification Report:")
# print(classification_report(y_test, y_pred))

# sample = np.array([[0.05, 0.05, 0.02, 0.03, -0.01,
#                     0.04, -0.02, 0.02, 0.03, 0.01]])

# prediction = model.predict(sample)

# if prediction[0] == 1:
#     print("Diabetic")
# else:
#     print("Not Diabetic")

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = KNeighborsRegressor(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))