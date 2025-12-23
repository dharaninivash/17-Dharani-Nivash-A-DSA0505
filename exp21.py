import pandas as pd

df = pd.DataFrame({'Name': ['Python', 'Pandas', 'NumPy']})
df['Name'] = df['Name'].str.swapcase()
print(df)
