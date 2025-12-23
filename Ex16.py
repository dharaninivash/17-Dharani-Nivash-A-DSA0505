import pandas as pd
data = {'School':['A','A','B'],'Age':[12,13,14]}
df = pd.DataFrame(data)
grp = df.groupby('School')
print(type(grp))
