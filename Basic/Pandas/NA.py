'''
Return Bool Array
    df.notnull()
    df[col].notnull()
Return Bool - Is Any
    df[col].isnull().any()
    df[col].notnull().all()
Delete Line
    df.dropna(column)     # delete line with na
        column : (default:all)
    df.drop_duplicates(column, keep)
        column : (default:all)
        keep : {'first', 'last', False}

Fill NA
    df.fillna(value, inplace=False)    # fill na with value
    df[col].fillna(..)
        inplace : operate on raw object or not (defult:False)

Drop Duplicates
'''
import pandas as pd
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, np.nan]])
data = pd.DataFrame(arr, columns=['col1', 'col2', 'col3'])

print(data['col3'].notnull())
print(data['col3'].notnull().any())



# print(data.notnull())
# print(data.dropna())