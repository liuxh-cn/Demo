'''
推荐使用 DafaFrameming.loc[行名, 列名] = 值 的方式去赋值
'''
import pandas as pd


df = pd.read_csv('section3-dau.csv')
print(df[:11])
result = df.loc[[9,10], 'user_id']
print(result)



