from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
import numpy as np


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion: ", confusion_matrix(y_test, y_pred))
print( classification_report(y_test, y_pred))

sample= np.array([[5.1, 3.5, 1.4, 0.2 ]])
pred = model.predict(sample)

print("model sample:",pred)
print("model sample:",pred)


new = [[4.1,3.2,1.4,6.1]]



