'''
Pack corresponding elements in iterable object into a tuple,
Then, use these tuples to form an array to return
'''
x = [[1, 1], [3, 8], [2, 9]]
y = [1, 1, -1]
train = zip(x, y)
# print(list(train))
for i in train:
    print(i)

