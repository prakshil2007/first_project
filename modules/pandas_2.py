import pandas as pd

data = {'Name': ['Anna', 'Bob', "charlie"],
        'Age' : [25, 30, 35]}

df = pd.DataFrame(data)
print(df.describe())