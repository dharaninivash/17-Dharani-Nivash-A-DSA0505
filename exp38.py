import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima'],
    'score': [12.5, np.nan],
    'attempts': [1, 3],
    'qualify': ['yes', 'no']
}

labels = ['a', 'b']

df = pd.DataFrame(exam_data, index=labels)
print(df)
