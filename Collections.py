from collections import OrderedDict as od, Counter, namedtuple, ChainMap
# OrderedDict and dictionaries
a = [('a', 1), ('z', 34), ('b', 2), ('c', 3)]
d = od(a)  # create and ordered dictionary from a list of tuples
print(d)   # --> OrderedDict([('a', 1), ('z', 34), ('b', 2),('c', 3)])
d['r'] = '67' # add to the OrderedDict like an ordinary dict()
g = d.keys()  # the keys() method works on it
print(d['a'])  # --> 1 can be accessed with keywords
print(g)      # --> odict_keys(['a', 'z', 'b', 'c', 'r'])
print(d.values())  # --> odict_values([1, 34, 2, 3, '67']) values() method work also
e = dict(d)
print(e)  # --> {'a': 1, 'z': 34, 'b': 2, 'c': 3, 'r': '67'} can be converted to a dictionary

# alternative ways of creating dictionaries
w = dict(a=9,b=6,v=7)
r = dict([('a', 6), ('t', 9), ('y', 67)])

# merging two dicts
print(w)  # --> {'a': 9, 'b': 6, 'v': 7}
print(r)  # --> {'a': 6, 't': 9, 'y': 67}
c = {**w, **r}  # syntactic sugar for merging two dictionaries and creating new dictionary
# when two keys are in both dicts the second key is used

r.update(w)  # when two keys are in both dicts the key in the dictionary calling the method is used
print(c)  # --> {'a': 6, 'b': 6, 'v': 7, 't': 9, 'y': 67}
print(r)  # ---> {'a': 9, 't': 9, 'y': 67, 'b': 6, 'v': 7}
n = w.setdefault('yu',68)       # adds new item to dict, returns value if key already in dict.
b = w.get('o', 9)    # does not add to dict() if key not in dict()
w['yu'] = w.get('yu')-8

# Counter Dictionaries
# this creates a dictionary that returns a dictionary sorted in descending order of frequency showing
# the number of times an item occurs in an iterable
b='rfoireoosjjfototieldkfkorpwprkgptktprkptktjtootktptktpktktotktotkotktototptktootptoro'
bc = Counter(b)
print(bc)  # --> Counter({'t': 24, 'o': 17, 'k': 14, 'p': 9, 'r': 6, 'f': 3, 'j': 3, 'i': 2,
				#  'e': 2, 's': 1, 'l': 1, 'd': 1, 'w': 1, 'g': 1})

# Counter objects support dictionary methods.
#  Counters can be used to check if two words are Anagrams
a = 'anagram'
c = 'gramana'
print(Counter(a)==Counter(c))

