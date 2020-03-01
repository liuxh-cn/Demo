'''
df.notnull()    # return dataframe with bool
df.dropna(column)     # delete line with na
    column : (default:all)
df.drop_duplicates(column, keep)
    column : (default:all)
    keep : {'first', 'last', False}

df.fillna(value, inplace=False)    # fill na with value
    inplace : operate on raw object or not (defult:False)
'''
import pandas as pd
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, np.nan]])
data = pd.DataFrame(arr, columns=['col1', 'col2', 'col3'])

print(data)
data = data.fillna(0)
print(data)


# print(data.notnull())
# print(data.dropna())