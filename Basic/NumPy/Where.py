'''
Dimension:
    1st dimension is the outermost array [[], [],..]
    nst dimension is the innermost array [0, 2]
# condition is a boolean expression
np.where(condition)
    return the coordinate of element satisfied with the condition in the format of tuple which consists of array
np.where(condition, x, y)
    if condition is true, then return x in corresponding position of the array
    else, return y there
'''
import numpy as np

n = np.array([[0, 2], [1, 0], [7, 0]])
print(np.where(n > 2))

print(np.where(n > 2, 1, -1))