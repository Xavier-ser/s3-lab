"""Matplotlib plotting exercises.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 02_matplotlib_programs.py
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



def matplotlib_programs():
    while True:
        print("\n--- MATPLOTLIB PROGRAMS ---")
        print("1. Dotted red line with green markers")
        print("2. Temperature vs sales line plot")
        print("3. Plot two lines with legend")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            x = [1, 2, 6, 18]
            y = [3, 10, 12, 20]
            plt.plot(x, y, color="red", marker="v", mfc="green",
                     mec="green", linestyle=":")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Line Plot")
            plt.grid(True)
            plt.show()

        elif choice == "2":
            temperature = [12, 14, 16, 18, 20, 22, 24]
            sales = [100, 200, 250, 400, 300, 450, 500]
            plt.plot(temperature, sales, marker="o")
            plt.xlabel("Temperature")
            plt.ylabel("Sales")
            plt.title("Temperature vs Sales")
            plt.grid(True)
            plt.show()

        elif choice == "3":
            days = [1, 2, 3, 4, 5]
            high = [30, 32, 31, 32, 33]
            low = [27, 26, 29, 28, 29]
            plt.plot(days, high, marker="o", label="Highest Temperature")
            plt.plot(days, low, marker="o", label="Lowest Temperature")
            plt.xlabel("Day")
            plt.ylabel("Temperature")
            plt.title("Temperature Difference")
            plt.legend()
            plt.show()

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    matplotlib_programs()
