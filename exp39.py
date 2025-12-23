import pandas as pd
import numpy as np

data = {
    'name': ['A','B','C','D'],
    'score': [10, 20, np.nan, 40]
}

df = pd.DataFrame(data)
print(df.head(3))
