import pandas as pd
import numpy as np


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                  'key2': ['one', 'two', 'one', 'two', 'one'],
                  'data1': np.random.randint(1, 10, 5),
                  'data2': np.random.randint(1, 10, 5)})

print(df)
grouped = df['data1'].groupby(df['key1']).mean()
print(grouped)