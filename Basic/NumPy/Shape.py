'''
-1  : unspecified value
    : the last element in the array
.reshape(row, column)
    (-1,1): to reshape data into 1 column without considering the number of columns
arr[a, -1]: [a, -1)

.shape
    a Property of an numpy array,
    Return a tuple to show levels of its each dimension
'''
import numpy as np

a = [[1, 1], [2, 2], [2, 5]]
a = np.array(a)
print(a.shape)
print(a.shape[0])

a_new = a.reshape(-1, 1)
print(a_new)

a_new = a.reshape(1, -1)[0]
print(a_new[1:2])