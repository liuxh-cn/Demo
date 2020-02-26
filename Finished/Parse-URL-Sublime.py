import re

str = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=touch&version_name=999.9&platformid=1&cateId=20&newcate=1&limit=20&offset=0&cityId=1&ci=1&startendday=20200226~20200226&startDay=20200226&endDay=20200226&q=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&ste=_b400202&mypos=36.268573%2C120.026409&attr_28=129&sort=defaults&uuid=9E0837307CECF698904A71598B5EF6E62E51F09DE81CB50A6E3AB94BA774B747&accommodationType=1&lat=36.268573&lng=120.026409&keyword=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6'
new_line = '\r\n'

p1 = r'(.*)\?(.*)'
r1 = re.match(p1, str)
host = r1.group(1)
new_str = '{0} ? {1}'.format(host, new_line)
args = r1.group(2)
p2 = r'([^=]*)=([^&]*)&?'
r2 = re.findall(p2, args)
for i in r2:
    new_str = '{0}{1} : {2}{3}'.format(new_str, i[0], i[1], new_line)
print(new_str)
