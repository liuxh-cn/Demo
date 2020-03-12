'''
np.
    sum/cumsum(arr)
    prod/cumprod(arr)
    mean(): get average value
    var(): get variance
    std(): get standard variance
    log(): get ln ← np.e
    log10(): ..


'''
import numpy as np

arr = np.arange(1, 10)
print(arr)
result = np.sum(arr)
result = np.cumsum(arr)
result = np.prod(arr[:3])
result = np.cumprod(arr)
result = np.var([1, 1, 1])
result = np.var([1, 4, 1])
result = np.log(np.e)
print(np.e)
print(result)