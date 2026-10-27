"""Converted from matrix.ipynb."""

# 2x2 matrix using initialization<br>

import numpy  as np

import numpy  as np
m1=np.array([[1,2],[3,4]])
m2=np.array([[2,4],[6,8]])
print("Dot: \n",m1.dot(m2))
print("transpose: \n",np.transpose(m1))
print("inverse\n",np.linalg.inv(m1))
print("determinant\n",np.linalg.det(m1))
print("1D array\n",m1.flatten())

# matrix from user

matrix=[]
x=int(input("enter no of rows:"))
y=int(input("enter no of columns:"))
for i in range(x):
    row=[]
    for j in range(y):
        row.append(int(input()))
    matrix.append(row)
m1=np.array(matrix)
m1
print("transpose  \n" ,np.transpose(m1))

# 2nd way- user input matrix using list,map,split

matrix=[]
x=int(input("enter no of rows:"))
y=int(input("enter no of columns:"))
a=list(map(int,input().split()))
matrix.append(a)
m1=np.array(matrix)
m1=m1.reshape(x,y)
m1

# <h1>Ex 2</h1>
# <h5>Write a program to create 2 matrix from user and find the following
# <ul><li>dot product</li>
# <li>transpose</li>
# <li>determinant</li>
# <li>inverse</li>
# <li>trace  .trace</li>
# <li>rank matrix_rank</li>
# <li>Eigen values and Eigeen vectors  eig</li></ul></h5>

import numpy as np
matrix1=[]
matrix2=[]
r1,c1=list(map(int,input("Enter no of rows and cols for matrix 1:").split()))
r2,c2=list(map(int,input("Enter no of rows and cols for matrix 2:").split()))
m=list(map(int,input("Enter elements of matrix 1:").split()))
matrix1.append(m)
m1=np.array(matrix1).reshape(r1,c1)
m=list(map(int,input("Enter elements of matrix 2:").split()))
matrix2.append(m)
m2=np.array(matrix2).reshape(r2,c2)
print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
dot=m2.dot(m1)
print("\nDot Product:")
print(dot)
print("\nTranspose of matrix 1:")
print(np.transpose(m1))
print("\nDeterminant of matrix 2")
print(np.linalg.det(m1))
print("\nInverse of matrix 2:")
print(np.linalg.inv(m2))
print("\nTrace of matrix 1")
print(m1.trace())
print("\nRank of matrix 1")
print(np.linalg.matrix_rank(m1))
print("\nEigen Values of matrix 1")
print(np.linalg.eig(m2))
