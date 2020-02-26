arr = ['a', 'b', 'c']

# Method -1. Fault Case for example
for i in arr:
    i = '<' + i + '>'
print(arr)

arr = ['a', 'b', 'c']
# Method 1.
for i in range(0, len(arr)):
    arr[i] = '<' + arr[i] + '>'
print(arr)

arr = ['a', 'b', 'c']
# Method 2. Use Build-in Func Map(func, arr) & list(iterator)
def func(x):
    return '<' + x + '>'
arr = map(func, arr)
print(list(arr))
