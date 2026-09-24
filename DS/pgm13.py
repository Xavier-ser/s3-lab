# python pgm to read no. of rows and cols for matrix1 
# create matrix1 
# read rows and cols for matrix2 and create matrix2
# find dot product and transpose of matrix1 and matrix2, trace of matrix1 and matrix2 
# find rank of matrix 1 and matrix2 
# determinent of matrix1
# inverse of matrix2

import numpy as np

r1 = int(input("Enter rows of matrix1: "))
c1 = int(input("Enter columns of matrix1: "))

matrix1 = np.array([
    list(map(int, input(f"Enter row {i+1}: ").split()))
    for i in range(r1)
])

r2 = int(input("Enter rows of matrix2: "))
c2 = int(input("Enter columns of matrix2: "))

matrix2 = np.array([
    list(map(int, input(f"Enter row {i+1}: ").split()))
    for i in range(r2)
])

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

if c1 == r2:
    print("\nDot Product:")
    print(np.dot(matrix1, matrix2))
else:
    print("\nDot product not possible")

print("\nTranspose of Matrix 1:")
print(matrix1.T)

print("\nTranspose of Matrix 2:")
print(matrix2.T)

if r1 == c1:
    print("\nTrace of Matrix 1:", np.trace(matrix1))
    print("Determinant of Matrix 1:", np.linalg.det(matrix1))
else:
    print("\nTrace and determinant of Matrix 1 require a square matrix")

if r2 == c2:
    print("\nTrace of Matrix 2:", np.trace(matrix2))
    print("Determinant of Matrix 2:", np.linalg.det(matrix2))
    
    if np.linalg.det(matrix2) != 0:
        print("\nInverse of Matrix 2:")
        print(np.linalg.inv(matrix2))
    else:
        print("\nInverse of Matrix 2 does not exist")
else:
    print("\nTrace and inverse of Matrix 2 require a square matrix")

print("\nRank of Matrix 1:", np.linalg.matrix_rank(matrix1))
print("Rank of Matrix 2:", np.linalg.matrix_rank(matrix2))