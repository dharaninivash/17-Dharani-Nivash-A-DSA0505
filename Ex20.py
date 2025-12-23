import pandas as pd
df = pd.DataFrame({'Name':['Python','Pandas','NumPy']})
print(df['Name'].str.find('da'))
