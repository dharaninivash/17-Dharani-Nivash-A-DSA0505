import pandas as pd
import numpy as np

data = {
    'name': ['A','B','C'],
    'score': [10, np.nan, 30],
    'attempts': [1,2,3]
}

df = pd.DataFrame(data)
print(df[['name', 'score']])
