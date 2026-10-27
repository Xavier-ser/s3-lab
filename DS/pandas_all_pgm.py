import pandas as pd


# ============================================================
# PROGRAM 1: CREATE A SERIES FROM A LIST
# ============================================================

print("\nPROGRAM 1: CREATE A SERIES FROM A LIST")

# Create a Python list
numbers = [10, 20, 30, 40, 50]

# Convert the list into a Pandas Series
s = pd.Series(numbers)

# Display the Series
print(s)


# ============================================================
# PROGRAM 2: CREATE A SERIES OF DATES
# ============================================================

print("\nPROGRAM 2: CREATE A SERIES OF DATES")

# Generate five dates starting from 1 January 2026
dates = pd.date_range(start="2026-01-01", periods=5)

# Display the dates
print(dates)


# ============================================================
# PROGRAM 3: CREATE A DATAFRAME FROM A DICTIONARY
# ============================================================

print("\nPROGRAM 3: CREATE A DATAFRAME FROM A DICTIONARY")

# Create a dictionary containing student details
data = {
    "Name": ["Arun", "Binu", "Cathy", "David"],
    "Age": [20, 21, 19, 22],
    "Mark": [85, 90, 78, 88]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# ============================================================
# PROGRAM 4: CREATE A DATAFRAME FROM A TWO-DIMENSIONAL LIST
# ============================================================

print("\nPROGRAM 4: CREATE A DATAFRAME FROM A 2D LIST")

# Create a two-dimensional list
data = [
    ["Arun", 20, 85],
    ["Binu", 21, 90],
    ["Cathy", 19, 78],
    ["David", 22, 88]
]

# Create a DataFrame and specify column names
df = pd.DataFrame(data, columns=["Name", "Age", "Mark"])

# Display the DataFrame
print(df)


# ============================================================
# PROGRAM 5: CREATE A CSV FILE AND READ IT
# ============================================================

print("\nPROGRAM 5: CREATE AND READ A CSV FILE")

# Create a dictionary containing employee details
data = {
    "Name": ["Arun", "Binu", "Cathy", "David"],
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [30000, 25000, 40000, 35000]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
# index=False prevents Pandas from saving the row index
df.to_csv("employees.csv", index=False)

print("CSV file created successfully!")

# Read the CSV file into a DataFrame
df = pd.read_csv("employees.csv")

# Display the contents of the CSV file
print(df)


# ============================================================
# PROGRAM 6: SORT A DATAFRAME AND RESET ITS INDEX
# ============================================================

print("\nPROGRAM 6: SORT AND RESET INDEX")

# Create a DataFrame
data = {
    "Name": ["Arun", "Binu", "Cathy", "David"],
    "Salary": [30000, 25000, 40000, 35000]
}

df = pd.DataFrame(data)

# Sort the DataFrame by Salary in ascending order
sorted_df = df.sort_values(by="Salary")

print("After sorting:")
print(sorted_df)

# Reset the index and remove the old index
sorted_df = sorted_df.reset_index(drop=True)

print("After resetting the index:")
print(sorted_df)

# Display the first two rows using iloc
print("First two rows:")
print(sorted_df.iloc[0:2])


# ============================================================
# PROGRAM 7: FIND AVERAGE SALARY USING GROUPBY()
# ============================================================

print("\nPROGRAM 7: AVERAGE SALARY BY DEPARTMENT")

# Create employee data
data = {
    "Name": ["Arun", "Binu", "Cathy", "David", "Eva"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [30000, 25000, 40000, 35000, 50000]
}

df = pd.DataFrame(data)

# Group employees by department
# Calculate the average salary of each department
average_salary = df.groupby("Department")["Salary"].mean()

# Display the result
print(average_salary)


# ============================================================
# PROGRAM 8: HANDLE MISSING VALUES USING fillna()
# ============================================================

print("\nPROGRAM 8: FILL MISSING VALUES")

# Create a DataFrame containing missing values
data = {
    "Name": ["Arun", "Binu", "Cathy", "David"],
    "Mark": [85, None, 78, None]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing marks with zero
df["Mark"] = df["Mark"].fillna(0)

print("After filling missing values:")
print(df)


# ============================================================
# PROGRAM 9: CONVERT A COLUMN INTO BOOLEAN VALUES
# ============================================================

print("\nPROGRAM 9: CONVERT PROFIT INTO BOOLEAN VALUES")

# Create a DataFrame
data = {
    "Company": ["A", "B", "C", "D"],
    "Profit": [10000, -5000, 8000, -2000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Convert profit values into Boolean values
# True means profit is greater than zero
# False means profit is zero or less
df["Profit"] = df["Profit"] > 0

print("After converting Profit into Boolean values:")
print(df)


# ============================================================
# PROGRAM 10: MERGE TWO DATAFRAMES
# ============================================================

print("\nPROGRAM 10: MERGE TWO DATAFRAMES")

# Create the first DataFrame
data1 = {
    "ID": [1, 2, 3, 4],
    "Name": ["Arun", "Binu", "Cathy", "David"]
}

df1 = pd.DataFrame(data1)

# Create the second DataFrame
data2 = {
    "ID": [1, 2, 3, 5],
    "Mark": [85, 90, 78, 95]
}

df2 = pd.DataFrame(data2)

print("First DataFrame:")
print(df1)

print("Second DataFrame:")
print(df2)

# Merge both DataFrames using the common ID column
# Inner join keeps only IDs present in both DataFrames
merged_df = pd.merge(df1, df2, on="ID", how="inner")

print("Merged DataFrame:")
print(merged_df)


# ============================================================
# END OF ALL 10 PANDAS PROGRAMS
# ============================================================