import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(np.dot(A, B))

print("Transpose:")
print(A.T)

print("Determinant:", np.linalg.det(A))

print("Maximum value:", np.max(A))
print("Minimum value:", np.min(A))

print("Trace:", np.trace(A))