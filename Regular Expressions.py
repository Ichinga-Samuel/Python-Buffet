import re


st = 'My number is 415-555-4242.'
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = pattern.search(pattern)
mo = pattern.search(st)
mo.group()
# Out[7]: '415-555-4242'

pat = re.compile(r'(\d{3})-(\d{3}-\d{4})')
g = pat.search(st)
g.groups()
# Out[10]: ('415', '555-4242')
g.groups(0)
# Out[11]: ('415', '555-4242')
g.group(1)
# Out[12]: '415'
g.group(0)
# Out[13]: '415-555-4242'
g.group(2)
# Out[14]: '555-4242'
g.group()
# Out[15]: '415-555-4242'
name = 'My name is Ichinga Samuel'
pn = re.compile(r'Samuel|Ichinga')
gn = pn.search(name)
gn.group()
# Out[19]: 'Ichinga'
bat = 'The Adventures of Batwoman'
bname = 'My name is Ichinga Samuel. I am batman and i know batwoman'
bp = re.compile(r'bat(wo)+man')
bo = bp.search(bat)
bo.group()

bw = re.compile(r'bat(wo)*man')
wo = bw.search(bname)
wo.group()

date = '15th-june-2020'
da = re.compile(r'-')
da.sub('/', date)
# Out[150]: '15th/june/2020'

da = re.compile(r'(\w*)-(\w*)-(\w*)')
da.sub(r'\3_\2_\1', date)
# Out[159]: '2020_june_15th'
