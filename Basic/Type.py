import pandas as pd

# 1. view the type of data
data = pd.read_csv('./section3-dau.csv')
# print(type(data))
# print(data.dtypes)

# 2. change the type of data
## pandas
date = pd.to_datetime('2010-01-01') # to Timestamp
print('%s %s' % (type(date), date))
