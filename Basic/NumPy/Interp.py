'''
一维线性插值: 在[xp, fp]构成的线性序列里，获取x的一维线性插值
np.interp(x, xp, fp): return y


'''
import numpy as np
import matplotlib.pyplot as plt

x = 2.5
xp = [1, 2, 3]
fp = [3, 2, 0]

y = np.interp(x, xp, fp)
print(y)

plt.plot(xp, fp, '-o')
plt.plot(x, y, 'x')
plt.show()