'''
.shape
    a Property of an numpy array,
    Return a tuple to show levels of its each dimension
'''
import numpy as np

a = [[1, 1], [2, 2], [2, 5]]
a = np.array(a)

print(a.shape)
print(a.shape[0])