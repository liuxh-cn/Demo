'''
*\np.dot\np.multiply
    *:              multiply corresponding elements, to get a element-level product, different from that in Matlab
    np.dot:         Point Multiplication for 1 demision and Matrix Multiplication for n dimension
        multiply corresponding elements and then sum the results
    np.multiply:    multiply corresponding elements

Convolution Operation:
    np.sum(np.multiply(k, data[,]))
'''
import numpy as np
a = np.array([1,2,3])
b = a
print(a*b)
k = np.array([
    [0,1,2],
    [2,2,0],
    [0,1,2]
])
data = np.array([
    [3,3,2,1,0],
    [0,0,1,3,1],
    [3,1,2,2,3],
    [2,0,0,2,2],
    [2,0,0,0,1]
])
print(np.dot(k, k))
print(np.multiply(k, k))
print(k * k)