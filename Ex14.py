import pandas as pd
import numpy as np

# Create DataFrame with missing values
data = {
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
}

df = pd.DataFrame(data)

# Replace missing values with 0
df_filled = df.fillna(0)

print(df_filled)
