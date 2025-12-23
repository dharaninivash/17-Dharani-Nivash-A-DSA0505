import pandas as pd
import numpy as np
df = pd.DataFrame([[np.nan,np.nan,1],[1,2,3]])
print(df[df.isna().sum(axis=1) >= 2])
