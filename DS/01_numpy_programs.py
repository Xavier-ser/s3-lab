"""NumPy exercises: compare arrays, matrices, sums, file handling, row swap, multiplication.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 01_numpy_programs.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, tree
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score



def numpy_programs():
    while True:
        print("\n--- NUMPY PROGRAMS ---")
        print("1. Compare two arrays element-wise")
        print("2. Generate even numbers from 50 to 90")
        print("3. Create a 4x4 identity matrix")
        print("4. Create a 5x5 diagonal matrix with 1,2,3,4,5")
        print("5. Change signs of values from 9 to 15 in vector 0..20")
        print("6. Sum all elements, rows and columns")
        print("7. Save an array to a text file and read it")
        print("8. Check element-wise equality of two arrays")
        print("9. Create a random 4x4 matrix and swap first/last rows")
        print("10. Multiply two arrays element-by-element")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            a = np.array([1, 2, 3, 4])
            b = np.array([5, 6, 1, 7])
            print("A > B :", np.greater(a, b))
            print("A <= B:", np.less_equal(a, b))
            print("A >= B:", np.greater_equal(a, b))
            print("A < B :", np.less(a, b))
            print("A == B:", np.equal(a, b))

        elif choice == "2":
            print(np.arange(50, 91, 2))

        elif choice == "3":
            print(np.identity(4, dtype=int))

        elif choice == "4":
            print(np.diag([1, 2, 3, 4, 5]))

        elif choice == "5":
            vector = np.arange(0, 21)
            print("Original:", vector)
            vector[9:16] *= -1
            print("After changing signs:", vector)

        elif choice == "6":
            array = np.array([[1, 2], [5, 3]])
            print("Array:\n", array)
            print("Sum of all elements:", array.sum())
            print("Sum of each row:", array.sum(axis=1))
            print("Sum of each column:", array.sum(axis=0))

        elif choice == "7":
            array = np.arange(0, 10)
            np.savetxt("array.txt", array, fmt="%d")
            loaded = np.loadtxt("array.txt", dtype=int)
            print("Saved array to array.txt")
            print("Loaded array:", loaded)

        elif choice == "8":
            a = np.array([0, 10])
            b = np.array([0, 4])
            print("Element-wise equality:", np.equal(a, b))

        elif choice == "9":
            matrix = np.random.randint(2, 10, size=(4, 4))
            print("Original matrix:\n", matrix)
            matrix[[0, -1]] = matrix[[-1, 0]]
            print("After swapping first and last rows:\n", matrix)

        elif choice == "10":
            a = np.array([1, 2, 3, 4, 5])
            b = np.array([2, 3, 4, 5, 6])
            print("Array 1:", a)
            print("Array 2:", b)
            print("Element-wise product:", a * b)

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    numpy_programs()
