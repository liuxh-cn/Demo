'''
Build-in range() is quite same as arange() in numpy module
'''
import numpy as np

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