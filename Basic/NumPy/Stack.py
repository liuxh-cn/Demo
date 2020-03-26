'''
hstack((arr1, arr2, ..)): append new arrays at the end of arr1
增加行长
    arr1: (1,3)
    arr2: (1,3)
    res:  (1,6)
vstack((arr1, arr2, ..)): stack new arrays at the end of arr1
增加列高
    arr1: (3,2)
    arr2: (2,2)
    res:  (5,2)
'''
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
res = np.hstack((arr1, arr2))
res = np.vstack((arr1, arr2))
# print(res)
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([[7, 8], [9, 0], [0, 1]])
res = np.hstack((arr1, arr2))
res = np.vstack((arr1, arr2))
print(res)
