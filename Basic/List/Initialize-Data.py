'''
Build-in range() is quite same as arange() in numpy module
1.
np.linspace(a, b, n)  from [a, b) by the number of elements to create array
np.arange(a, b, step) from [a, b] by the step of elements to create array
2.
reshape(m, n)
3.
arr.append(np.nan) : insert 'nan' into the end of the list
'''
import numpy as np

# 1 np.arange(a, b, step) & range(a, b, step)
l = range(5)
l_interval = range(1, 6)
l_step = range(1, 6, 2)
print(list(l))
print(list(l_interval))
print(list(l_step))

nl = np.arange(5)
nl_interval = np.arange(1, 6)
nl_step = np.arange(1, 6, 2)
print(nl)
print(nl_interval)
print(nl_step)

# 2 np.linspace(a, b, n)
data = np.linspace(0, 10, 4)
print(data)

# 3
data = np.arange(6).reshape(2, 3)
