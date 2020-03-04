'''
Determine the relationship (equal or not) between two objects in Python
==、cmp()、is
assert_frame_equal(): print error once unequal values are detacted
'''
import operator
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

a = [1, 2, 3]
b = [2, 3, 4]
d = [1, 2, 3]
c = [i-1 for i in b]

# Operator '==' is used to compare 「values」 within variables
# which is totally different from or even opposite to the one in Java
print(a == c)
print(a == d)
# Keyword 'is' is used to make sure if two variables point to 「the same object」
print(a is c)
print(a is d)
# Build-in function operator.eq(), same as '==' in Python, compare values of two variable
print(operator.eq(a, c))
print(operator.eq(a, d))

# Compare DataFrame
df1 = pd.DataFrame(np.arange(12).reshape(3, -1))
df2 = pd.DataFrame(np.arange(12).reshape(3, -1))
assert_frame_equal(df1, df2)
df2.loc[2, 1] = 7
assert_frame_equal(df1, df2)