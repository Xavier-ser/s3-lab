import numpy as np
from numpy import linalg

# Function to read an n × n matrix from the user
def matrixread(n):

    # Empty list to store the matrix
    matrix = []

    # Loop through rows
    for i in range(n):

        # Temporary list for one row
        temp = []

        # Loop through columns
        for j in range(n):

            # Read one element from the user
            num = int(input("Enter element " + str(i) + "," + str(j) + ": "))

            # Add the number to the current row
            temp.append(num)

        # Add the completed row to the matrix
        matrix.append(temp)

    # Return the matrix
    return matrix


# Get the order of the matrix
n = int(input("Enter the order of the matrix: "))

# Read first matrix
print("Matrix 1")
matrix1 = np.array(matrixread(n))

# Read second matrix
print("Matrix 2")
matrix2 = np.array(matrixread(n))

# Display matrices
print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)


# -------------------------------
# 1. DOT PRODUCT
# -------------------------------

print("Dot Product =")
print(np.dot(matrix1, matrix2))


# -------------------------------
# 2. TRANSPOSE
# -------------------------------

print("Transpose of matrix 1 =")
print(np.transpose(matrix1))


# -------------------------------
# 3. TRACE
# -------------------------------

print("Trace of matrix 1 =")
print(np.trace(matrix1))


# -------------------------------
# 4. RANK
# -------------------------------

print("Rank of matrix 1 =")
print(linalg.matrix_rank(matrix1))


# -------------------------------
# 5. DETERMINANT
# -------------------------------

print("Determinant of matrix 1 =")
print(np.linalg.det(matrix1))


# -------------------------------
# 6. INVERSE
# -------------------------------

print("Inverse of matrix 1 =")
print(linalg.inv(matrix1))


# -------------------------------
# 7. EIGENVALUES AND EIGENVECTORS
# -------------------------------

print("Eigenvalues and Eigenvectors =")
print(linalg.eig(matrix1))