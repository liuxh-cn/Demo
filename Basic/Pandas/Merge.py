'''
pandas.merge : match connected keywords(left & right)
    inner/outer/left/right join
        left: 左侧包含右侧的全部情况，对左侧补充信息
        inner: 左侧包含右侧的情报情况，对右侧补充信息
    args : df1, df2, on(left_on, right_on, left_index, right_index), how, suffixex

'''
import pandas as pd
'''
  key  data1
0   b      0
1   b      1
2   a      2
3   c      3
4   a      4
  key  data2
0   a      0
1   b      1
2   d      2
'''
df1 = pd.DataFrame({'key': list('bbaca'), 'data1':range(5)})
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2':range(3)})

'''
inner join(default) : take the intersection of connected fields
'''
inner_join = pd.merge(df1, df2)
inner_join = pd.merge(df1, df2, on='key')
inner_join = pd.merge(df1, df2, left_on='key', right_on='key')
# print(inner_join)
# match left 'key' field and right index
inner_join = pd.merge(df1, df2, left_on='data1', right_index=True)
print(inner_join)
# use 'suffixex' to rename fields with same name
inner_join = pd.merge(df1, df2, left_on='data1', right_index=True, suffixes=['_df1', '_df2'])
print(inner_join)
'''
outer join : take the union of connected fields - union of results from both left join and right join
left join  : take keys in the left collection; fill empty position with NaN
right join : the same principle with left join
'''
outer_join = pd.merge(df1, df2, how='outer')
# print(outer_join)
left_join = pd.merge(df1, df2, how='left')
# print(left_join)
right_join = pd.merge(df1, df2, how='right')
# print(right_join)