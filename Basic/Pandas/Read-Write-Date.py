'''
pd.read_csv('.csv', args): DataFrame
    header=0: if the header exists or not(default: take the first line as header)
    names=[]: customize headers, always accompany 'header=None'
    index_col=None: designate certain column as index(exp. 0)
    parse_dates=False: if parse string to datetime or not

data.to_csv('.csv', args)
    index: if write the index of data. suggest 'None'(default: True)
'''
import pandas as pd

data = pd.read_csv('./aapl.csv')
print(data)
data.to_csv('aapl_2.csv', index=None)
print('ok')