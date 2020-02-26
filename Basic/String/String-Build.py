'''
note: str() is a function, don't use it as a name of a variable
'''
# Method 1. Use keyword '%' & '%s..'
s1 = 'hello'
s2 = 'world'
n = 123
result = '%s %s \n%d' % (s1, s2, n)
print(result)

# Method 2. Use func format & '{n}'
result = '{0} {1} \n{2}'.format(s1, s2, n)
print(result)

# Method 3. Use func join (only str not int .etc)
result = ' '.join([s1, s2, str(n)])
print(result)

# Method 4. Use signal '+' (only str not int .etc)
result = s1 + ' ' + s2 + ' ' + str(n)
print(result)