import pandas as pd

data = {
    'name': ["abs", "xyz", "pqr", "mno"],
    'age': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# print(df)

print(df.loc[0])