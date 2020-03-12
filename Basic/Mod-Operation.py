'''
x mod y: x%y
Modulus Operation is just like Remainder Operation
    with slight difference when x and y are different sign
'''
import numpy as np

arr = np.arange(7) + 1
for i in arr:
    print(i % 3)
