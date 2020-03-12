'''
Perceptron
Loss Function: Distance between points and line
Identify Misclassified Point:
    (np.dot(data, w) + b) * label <= 0
Random Gradient Descent:
    w = w + alpha * yi * xi
    b = b + alpha * yi
Note:
    完全一样的数据运行，结果可能不一样
'''
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[3, 3], [4, 3], [1, 1]])
label = np.array([1, 1, -1])
alpha = 1
w = np.array([0, 0])
b = 0
# y*(w*x+b)
f = (np.dot(data, w) + b) * label
idx = np.where(f <= 0)
iteration = 1
while f[idx].size != 0:
    point = np.random.randint(f[idx].shape[0])
    x = data[idx[0][point], :]
    y = label[idx[0][point]]
    w = w + alpha * y * x
    b = b + alpha * y
    print('Iteration:%d w:%s b:%s' % (iteration, w, b))
    f = (np.dot(data, w) + b) * label
    idx = np.where(f <= 0)
    iteration = iteration + 1

print(w, b)

# plot the line
x1 = np.arange(0, 6, 0.1)
x2 = (w[0] * x1 + b) / (-w[1])
plt.plot(x1, x2)

# plot the point
idx_p = np.where(label == 1)
idx_n = np.where(label != 1)
data_p = data[idx_p]
data_n = data[idx_n]

plt.scatter(data_p[:, 0], data_p[:, 1], color='red')
plt.scatter(data_n[:, 0], data_n[:, 1], color='blue')
plt.show()
