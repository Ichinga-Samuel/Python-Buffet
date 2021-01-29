import array
from collections import namedtuple, Counter, deque, OrderedDict, defaultdict, ChainMap


# array.array objects are mutable arrays but can only hold one type of data at a time. They support most list methods
# creating array.array object takes two two arguments the typecode to indicate the data type allowed and then the array
# creating an array.array object using the wrong typecode return an error
# ar = array.array('w', [2, 4])  # --> ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
arr = array.array('f', [1, 2, 4, 6])  # 'f' stands for floating point real numbers
# trying to append a string
# arr.append('sop')  # ----> TypeError: must be real number, not str
arr.append(8)  # ---> array('f', [1.0, 2.0, 4.0, 6.0, 8.0])
ars = array.array('i', (2, 4, 6, 7))  # 'i' all integers
# ars.append(9.09)  # --> TypeError: integer argument expected, got float

# Bytes are immutable sequence of single bytes (integers within the range 0 <= X < 256)
ab = bytes((1, 3, 5, 7, 9))   # --> b'\x01\x03\x05\x07\t'
#print(ab[1])  # --> 3
# bytes can not be more than 255
# ar = bytes((1, 3, 5, 7, 9, 259))  # --> ValueError: bytes must be in range(0, 256)

# Bytesarray object are like  byte objects but are mutable
ba = bytearray((1, 3, 5))  # --> bytearray(b'\x01\x03\x05')
# ba.append(278)  # --> ValueError: byte must be in range(0, 256)
# they can be converted back to bytes object
abb = bytes(ba)  # --> b'\x01\x03\x05'

# namedtuple
# namedtuples are data structures that are just like tuples but have field names that can be used to access the data
# stored in it.
p = namedtuple('Point', 'x y z')  # --> <class '__main__.Point'>
p1 = p(1, 3, 6)  # --> Point(x=1, y=3, z=6)

# Counter. These are special types of sets that allows for multiple occurrence of a set element.
fruits = Counter()
a = {'apple': 4, 'appricot': 6}
fruits.update(a)  # ---> Counter({'appricot': 6, 'apple': 4})
b = {'apple': 3, 'appricot': 7}
fruits.update(b)  # ---> Counter({'appricot': 13, 'apple': 7})

f = 'mississippi'
br = Counter('ppipssermm')
fr = Counter(f)   # ---> Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
#  print(len(fr))   # --> 4
# the length of a Counter object is the number of unique item it contains and not the total number of items
#print(sum(fr.values()))  # --> 11
# sorted(fr.elements()) returns all the elements in the counter sorted in ascending order showing their occurrences
# print(sorted(fr.elements()))    # ---> ['i', 'i', 'i', 'i', 'm', 'p', 'p', 's', 's', 's', 's']
# print(fr.most_common())  # ---> [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
br.subtract(fr)
#print(br)  # ---> Counter({'p': 1, 'e': 1, 'r': 1, 'm': 1, 's': -2, 'i': -3}) br changes
#print(fr)  # ---> Counter({'i': 4, 's': 4, 'p': 2, 'm': 1}) fr remains the same
br + fr    # adds two counters together
br - fr    # subtracts one counter from the other keeping only positive values
br & fr    # intersection of two counters
br | fr    # union of two counters
br['q'] += 1  # add and update an element


# deque (pronounced deck) they are double ended queues and can support appending and removing from the top and end in
# o(1) time there maximum length can be pre specified using maxlen kwarg
q = deque(['worship', 'code', 'eat', 'sleep'], maxlen=5)  # ---> deque(['worship', 'code', 'eat', 'sleep'])
q.append('pray')
q.remove('eat')
a = ['praise', 'study']
q.extendleft(a)  # adds new iterable items to the left of the deque but reversing the order of the iterable items
# --> deque(['study', 'praise', 'worship', 'code', 'sleep', 'pray'])
q.popleft()  # removes from the left
q.appendleft('adoration')

