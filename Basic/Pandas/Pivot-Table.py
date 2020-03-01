'''
Format Output
Once you used multiple 'groupby', you would think about 'pivot_table' as a better option
pd.pivot_table(args..)
    index
    value
    columns     additional segment - horizontal index
    aggfunc     aggregate function(list/dict)


'''
import pandas as pd

s = pd.Series(range(5))
print(s)