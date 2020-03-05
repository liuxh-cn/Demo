'''
Dimension: arr[1st, 2nd, .., nth]
    1st dimension is the outermost array [[], [],..]
    nth dimension is the innermost array [0, 2]
# condition is a boolean expression
np.where(condition)
    return the coordinate of element satisfied with the condition in the format of tuple which consists of array
np.where(condition, x, y)
    if condition is true, then return x in corresponding position of the array
    else, return y there
'''
import numpy as np

n = np.array([[[0, 2], 1], [[1, 0], -1], [[7, 0], 1]])
print(n[1, :])
print(n[1, 0])
print(n[1, 0][1])
print('--------------------')
n = np.array([[[0, 2], [1, 9]], [[1, 0], [-1, 9]], [[7, 0], [1, 8]]])
print(n.shape)
print(np.where(n > 3))
print('--------------------')
print(np.where(n > 2, 1, -1))
