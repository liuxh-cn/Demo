'''
all() & any()

'''
import pandas as pd
import numpy as np

r = np.array([[1, 2, 3], [1, 0, np.nan]])
print(r.all())
frame = pd.DataFrame(r, index=['0', '1'], columns=['col1', 'col2', 'col3'])
print(frame)
print(frame.notnull())








