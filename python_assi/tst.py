import re
st = "Hello From Othefr sid5e"
lst = re.findall('[a-z0-9]',st)
print(lst)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+?', x)
print(y)