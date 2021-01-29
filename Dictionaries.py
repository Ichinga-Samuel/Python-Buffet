import collections as co
from types import MappingProxyType


# Python Dictionaries
# dictionaries has O(1) time complexity for lookup, insert, update and delete operations in average cases
# there are some specialized dictionaries that are part of the core library but must be imported.

# OrderedDict: This special type of dictionary remembers the insertion order of the keys
d = co.OrderedDict(one=1, two=2, three=3)
c = dict(one=4, pop=6, lol=90)
# when creating keys which are strings in OrderedDict and dict don't put the keys in quotation signs ('')
print(d)  # --> OrderedDict([('one', 1), ('two', 2), ('three', 3)])
print(c)  # --> {'one': 4, 'pop': 6, 'lol': 90}
print(d['one'])  # --> use '' when accessing with the key
dc = dict(d)  # convert OrderedDict to dictionary
print(dc)   # --> {'one': 1, 'two': 2, 'three': 3}

# defaultdict
# defaultdict is a special type of dict that has a default_factory attribute. if present when creating the object it is
# initialized from the first argument to the constructor else it is set as None. it is usually a data type and takes
# care of missing keys.

dd = co.defaultdict()
print(dd)       # --> defaultdict(None, {})
dd['dog'] = 1
dd['goat'] = 2
an = list(dd.items())
#  print(dd['cow'])  # --> KeyError: 'cow' when default_factory is None an exception is thrown if the key is not found

dd = co.defaultdict(list)
for i, j in an:
    dd[i] = j

print(dd)  # --> defaultdict(<class 'list'>, {'dog': 1, 'goat': 2})
print(dd['cow'])
print(dd)  # --> defaultdict(<class 'list'>, {'dog': 1, 'goat': 2, 'cow': []})
# since the default_factory argument is list the missing key is added to the dictionary and its value is an empty lis
dd['lamb'].append(9)  # even if lamb is not in the dict it is created and a list is passed as a value to it which we can
# append 9
print(dd)
# default dict can be used for counting
a = 'bdggyfjkbfdhikfdgkgd'
wc = co.defaultdict(int)
for i in a:
    wc[i] += 1

print(wc)  # defaultdict(<class 'int'>, {'b': 2, 'd': 4, 'g': 4, 'y': 1, 'f': 3, 'j': 1, 'k': 3, 'h': 1, 'i': 1})

# ChainMap
# A ChainMap is a structure that groups dictionaries into a single mapping. We can search through the entire ChainMap
# but insertion, deletions and deleting can only be carried out on the first mapping.

di = dict(wc)
de = dict(dd)
mapping = co.ChainMap(de, di)
print(mapping)
# ChainMap({'dog': 1, 'goat': 2, 'cow': [], 'lamb': [9]}, {'b': 2, 'd': 4, 'g': 4, 'y': 1, 'f': 3, 'j': 1, 'k': 3,
#  'h': 1, 'i': 1})
m = list(mapping)
print(m)  # prints all the keys of the mapping in a list
print(mapping['f'])  # --> 3
mapping['y'] = 9
print(mapping)
# ChainMap({'dog': 1, 'goat': 2, 'cow': [], 'lamb': [9]}, {'b': 2, 'd': 4, 'g': 4, 'y': 1, 'f': 3, 'j': 1,
#  'k': 3, 'h': 1, 'i': 1}) no change to y because it is in the second mapping
mapping['goat'] = 9
print(mapping)
# ChainMap({'dog': 1, 'goat': 9, 'cow': [], 'lamb': [9], 'y': 9}, {'b': 2, 'd': 4, 'g': 4, 'y': 1, 'f': 3,
#  'j': 1, 'k': 3, 'h': 1, 'i': 1}) goat has been changed to 9 because it is in the first mapping also the new object
# y is added to the first mapping since it is not found in the first mapping and hence can not be updated

dw = {'w': 4, 'k': 5}
ds = {'w': 2, 'g': 4}
mp = co.ChainMap(dw, ds)
print(mp)  # --> ChainMap({'w': 4, 'k': 5}, {'w': 2, 'g': 4})
print(mp['w'])  # --> 4
# if two dicts has the same keys they appear on both mappings but only the first one can be accessed

# MappingProxyTypes produces dictionaries that are read only. new keys can not be added and the value of existing ones
# cannot be modified
mp = {i: i*2 for i in range(1, 12)}
mpt = MappingProxyType(mp)
print(mpt, type(mpt))  # --> {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}
# mpt['12'] = 24  # --> TypeError: 'mappingproxy' object does not support item assignment
# mpt[11] = 33  # --> TypeError: 'mappingproxy' object does not support item assignment
# Any change on the dictionary used in creating the MappingProxyType object be reflected on the MappingProxyType object
mp[11] = 33
mp['12'] = 'Twenty_Four'
print(mpt)  # --> {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 33, '12': 'Twenty_Four'}
# the changes in mp is implemented in mpt



