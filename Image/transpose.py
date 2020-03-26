'''
new_nping = np.transpose(nping, (new_index))
vs: nping.shape vs new_nping.shape

i = iter(x)
value = i.next()

nping = torchvision.utils.make_grid(image_list, nrow=8, padding=2)
vs: image_list.shape vs nping.shape
    return: turn 4D data into 3D
        Connect a list of images together
    nrow=8: Number of images displayed in each row of the grid
    padding: 单个图像四周的填充区域宽度
    pad_value=0: Value for the padded pixels, default: 0 (black)
'''
import numpy as np
import torchvision
import torchvision.transforms as transforms
import torch
import matplotlib.pyplot as plt

'''
改变索引序列：
二维数组改变索引序列就是转置 (0,1) - (1,0) 类似 (x,y) - (y,x)
三维数组改变索引序列需要指定新的索引序列 (0,1,2) - (...)
典型应用：
    三维图像数组 (channels,x,y) - (x,y,channels)
    
典型表现：
    1 the change of numpy shape
        (2,2,3) to (2,3,2)
    2 the change of coordinate of elements
        exp. 7 (1,0,1) to (0,1,1)
'''

'''1 Simple'''
'''
[[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
'''
x = np.arange(12).reshape((2,2,3))
x = np.transpose(x, (1,2,0))
# print(x)
'''
x.shape
(2,3,2)

x
[[[ 0  6]
  [ 1  7]
  [ 2  8]]

 [[ 3  9]
  [ 4 10]
  [ 5 11]]]
'''

'''2 Image'''
transforms = transforms.Compose(
    [transforms.ToTensor()]
)
trainset = torchvision.datasets.MNIST('/opt/dataset/MNIST',transform=transforms,train=True,download=False)
trainLoader = torch.utils.data.DataLoader(trainset,shuffle=False,batch_size=4)

dataiter = iter(trainLoader)
images, labels = dataiter.next()
print(images.shape)
nping = torchvision.utils.make_grid(images, padding=0).numpy()
print(nping.shape)
new_nping=np.transpose(nping, (1,2,0))
plt.imshow(new_nping)
print(new_nping.shape)
plt.show()
