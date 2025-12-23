import pandas as pd
data = {
    'School': ['A', 'A', 'B', 'B', 'C'],
    'Age': [12, 13, 14, 15, 16]
}
df = pd.DataFrame(data)
result = df.groupby('School')['Age'].agg(['mean', 'min', 'max'])
print(result)
