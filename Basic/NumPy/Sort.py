'''
np.argsort(arr, axis=1): return index of sorted element(same shape with input arr)
    arr: ASC(Default), DESC(-arr)
    axis: sort by 1-rows 0-columns
'''
import numpy as np

B = np.array([[4, 2, 3, 55], [5, 6, 37, 8], [-7, 68, 9, 0]])
print('B:')
print(B)
# 正序
# step1：
print('')
print('正序的时候')
print('默认输出')
print(np.argsort(B))  # 默认的输出每行元素的索引值。这些索引值对应的元素是从小到大排序的。

# step2：
print('axis=0时候的输出')
print(np.argsort(B, axis=0))  # 默认的输出每列元素的索引值。这些索引值对应的元素是从小到大排序的。

# step3:
print('axis=1的时候的输出')
print(np.argsort(B, axis=1))  # 默认的输出每行元素的索引值。这些索引值对应的元素是从小到大排序的。

# 逆序
print('')
print('逆序的时候')
# step1：
print('默认输出')
print(np.argsort(-B))  # 默认的输出每行元素的索引值。这些索引值对应的元素是从小到大排序的。

# step2：
print('axis=0时候的输出')
print(np.argsort(-B, axis=0))  # 默认的输出每列元素的索引值。这些索引值对应的元素是从小到大排序的。

# step3:
print('axis=1的时候的输出')
print(np.argsort(-B, axis=1))