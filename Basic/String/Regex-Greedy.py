'''
greedy mode vs non-greedy mode
Meanwhile, introduce 'reverse match' - a useful notion to solve this kind of question
'''
import re

# example 1.
url = 'utm_medium=touch&version_name=999.9&'
p1 = '([^=]*)=([^&]*)&?'        # reverse match - a useful notion
p2 = '(.*)=(.*)&'               # greedy mode(default)
p3 = '(.*?)=(.*?)&'             # non-greedy mode

result1 = re.findall(p1, url)
result2 = re.findall(p2, url)
result3 = re.findall(p3, url)
print(result1)
print(result2)
print(result3)

# example 2.
html = 'aa<div>test1</div>bb<div>test2</div>cc '
p2 = '<div>(.*?)</div>'

result = re.search(p2, html)
print(result.group(0))