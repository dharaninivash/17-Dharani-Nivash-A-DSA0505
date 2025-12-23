import numpy as np
import pandas as pd

df = pd.DataFrame([[1,2,np.nan],[4,np.nan,6]])
print(df.isna())
