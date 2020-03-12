'''
filter(func, seq): act on list
apply(func): act on Series generally or the whole DataFrame
    traverse the whole Series or DataFrame, and
    run specified function on 「each」 element

https://www.jianshu.com/p/4fdd6eee1b06
'''
import pandas as pd
import numpy as np
pd.set_option('display.width', 400)

# filter(func, seq)
divide_by_three = lambda x : True if x % 3 == 0 else False
selected_numbers = filter(divide_by_three, range(1, 11))
# print(list(selected_numbers))

# series.apply(func)
data = pd.read_csv('student-score.csv', sep=' +')
data['ExtraScore'] = data['Nationality'].apply(lambda x: 5 if x != '汉' else 0)
data['TotalScore'] = data['Score'] + data['ExtraScore']
# print(data)

data['NameLength'] = data['Name'].apply(len)
# print(data)

# to get proportion/ratio of each value to the column
df = pd.read_csv('Price.csv', sep=' +', index_col=0)
# print(df)
s = np.sum(df['Prices'])
df['ratio'] = df['Prices'].apply(lambda x: x/s)
print(df)
print(np.sum(df['ratio']))
