'''
Determine the relationship (equal or not) between two objects in Python
==、cmp()、is
'''
import operator

a = [1, 2, 3]
b = [2, 3, 4]
d = [1, 2, 3]
c = [i-1 for i in b]

# Operator '==' is used to compare 「values」 within variables
# which is totally different from or even opposite to the one in Java
print(a == c)
print(a == d)
# Keyword 'is' is used to make sure if two variables point to 「the same object」
print(a is c)
print(a is d)
# Build-in function operator.eq(), same as '==' in Python, compare values of two variable
print(operator.eq(a, c))
print(operator.eq(a, d))

