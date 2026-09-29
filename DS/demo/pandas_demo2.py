from sklearn import datasets

iris = datasets.load_iris()

print(iris.data[:5])
print(iris.target_names)
print(iris.target)

print(len(iris.data))

print(iris.feature_names)

print(len(iris.feature_names))

