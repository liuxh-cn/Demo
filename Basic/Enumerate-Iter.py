'''
enumerate()
    e.g.
        for idx, x in enumerate(x):
            idx & value
iter()
    e.g.

'''
import numpy as np
import matplotlib.pyplot as plt

X= np.array([6, 8, 10, 14, 18])
y = np.array([7, 9, 13, 17.5, 18])
yr = np.array([7.82327586, 9.77586207, 11.72844828, 15.63362069, 19.5387931 ])

plt.figure()
plt.plot(X, yr, 'k-')
for idx, x in enumerate(X):
    # print('%d - %d' % (idx, x))
    plt.plot([x, x], [y[idx], yr[idx]], 'r.-')
# plt.show()

'''simple display of enumerate()'''
for idx, x in enumerate(X):
    print('%d - %d' % (idx, x))
'''simple display of iter()'''
for i in iter(X):
    print('%d' % (i))