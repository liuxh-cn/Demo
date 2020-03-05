'''
Construct Index by means of grouped field/fields
    .groups(): view groups
    .get_group(key): return a dataframe
# grouped = df.groupby(col)
Aggregations
    grouped.agg(np.mean)
        np.size: view size of groups
        np.sum
        np.std:
    grouped[col].agg([np.mean, np.size, ..])
Transform: result share the same index with raw df
    grouped[col].transform(lambda x: x.mean())
'''
import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
grouped = df.groupby('Team')
print(grouped.groups)
result = grouped['Points'].transform(lambda x: x.mean())
print(result)
