import pandas as pd
data = {'School':['A','A','B'], 'Class':[1,2,1]}
df = pd.DataFrame(data)
print(df.groupby(['School','Class']).size())
