'''
View date type of each column
    df.dtypes
Mutual Conversion:
    datetime ↔ str
        pd.to_datetime(series)
        df['col'].dt.strftime(format)
        df['col'].map(lambda x: x.strftime(format))
'''
import pandas as pd

# 1. view the type of data
print('-------------------[1]-------------------')
data = pd.read_csv('section3-dau.csv')
print(data.dtypes)
# 2. str → datetime
print('-------------------[2]-------------------')
data.log_date = pd.to_datetime(data.log_date)
print(data.dtypes)
print(data.log_date[:5])
# 3.1 datetime → str
print('-------------------[3.1]-------------------')
result = data['log_date'].dt.strftime('%Y-%m')
print(result.dtypes)
print(result[:5])
# 3.2 datetime → str
print('-------------------[3.2]-------------------')
result = data['log_date'].map(lambda x:x.strftime('%Y-%m'))
print(result.dtypes)
print(result[:5])

