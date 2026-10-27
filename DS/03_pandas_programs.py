"""Pandas exercises: Series, DataFrames, CSV, selection, groupby, missing values, merge.

Install required packages once in terminal:
    python -m pip install numpy pandas matplotlib scikit-learn

Run this file directly:
    python 03_pandas_programs.py
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



def pandas_programs():
    while True:
        print("\n--- PANDAS PROGRAMS ---")
        print("1. Convert a list to a Series")
        print("2. Generate a date Series")
        print("3. Convert a dictionary to a DataFrame")
        print("4. Convert a 2D list to a DataFrame")
        print("5. Read a CSV file")
        print("6. Select rows/columns and display basic information")
        print("7. Group data and calculate mean")
        print("8. Handle missing values by replacing NaN with 0")
        print("9. Convert a numeric column to Boolean")
        print("10. Merge two DataFrames")
        print("0. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            values = [10, 20, 30, 40]
            series = pd.Series(values)
            print(series)

        elif choice == "2":
            dates = pd.date_range(start="2024-08-01", end="2024-08-15")
            print(dates)

        elif choice == "3":
            data = {"Name": ["Anu", "Binu", "Ciya"],
                    "Mark": [80, 75, 92]}
            df = pd.DataFrame(data)
            print(df)

        elif choice == "4":
            data = [[1, 2, 3], [4, 5, 6]]
            df = pd.DataFrame(data, columns=["A", "B", "C"])
            print(df)

        elif choice == "5":
            filename = input("Enter CSV filename (e.g. diabetes.csv): ").strip()
            try:
                df = pd.read_csv(filename)
                print(df)
                print("\nFirst five rows:\n", df.head())
            except FileNotFoundError:
                print("File not found. Put the CSV in the same folder as this .py file,")
                print("or enter its full path.")
            except Exception as error:
                print("Could not read the CSV:", error)

        elif choice == "6":
            df = pd.DataFrame({
                "Name": ["Anu", "Binu", "Ciya", "Dinu"],
                "Mark": [80, 75, 92, 68],
                "Course": ["MCA", "MCA", "BSc", "MCA"]
            })
            print("DataFrame:\n", df)
            print("\nFirst two rows:\n", df.head(2))
            print("\nMark column:\n", df["Mark"])
            print("\nShape:", df.shape)
            print("\nData types:\n", df.dtypes)

        elif choice == "7":
            df = pd.DataFrame({
                "Name": ["Alice", "Bob", "Charlie", "Dylan", "Emma"],
                "Job": ["Teacher", "Doctor", "Teacher", "Doctor", "Engineer"],
                "Salary": [25000, 55000, 20000, 35000, 65000]
            })
            print("Data:\n", df)
            print("\nAverage salary by job:\n", df.groupby("Job")["Salary"].mean())

        elif choice == "8":
            df = pd.DataFrame({"A": [1, 2, np.nan, 4],
                               "B": [np.nan, 2, 3, 4]})
            print("Before:\n", df)
            df = df.fillna(0)
            print("\nAfter replacing missing values with 0:\n", df)

        elif choice == "9":
            df = pd.DataFrame({"Company": ["A", "B", "C"],
                               "Profit": [1000, -500, 0]})
            df["Profit"] = df["Profit"] > 0
            print(df)

        elif choice == "10":
            df1 = pd.DataFrame({
                "ID": [101, 102, 103],
                "Name": ["John", "Amith", "Sona"],
                "Stipend": [30000, 35000, 20000]
            })
            df2 = pd.DataFrame({
                "ID": [101, 102, 103],
                "Position": ["Developer", "Developer", "Tester"]
            })
            result = pd.merge(df1, df2, how="inner", on="ID")
            print(result)

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    pandas_programs()
