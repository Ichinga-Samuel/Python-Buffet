import math
import collections
from array import array
import reprlib
import operator
import functools
import itertools as it
import numbers


@functools.total_ordering
class Vector(collections.abc.Sequence):
    typecode = 'd'
    coordinates = 'xyz'
    __slots__ = ('items', '__dict__')

    def __init__(self, items):
        self.items = array(self.typecode, items)

    @reprlib.recursive_repr(fillvalue='...')
    def __repr__(self):
        reprlib.maxother = 9
        r = reprlib.repr(self.items)
        return 'Vector({})'.format(r[r.find('[') + 1: -2])

    def __len__(self):
        return len(self.items)

    def __neg__(self):
        return Vector(-i for i in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            assert isinstance(other, Vector)
            pair = it.zip_longest(self, other, fillvalue=0)
            return Vector(i + j for i, j in pair)
        except AssertionError:
            return f'Can not add object of type {type(other)} with {type(Vector)} object '

    def __sub__(self, other):
        return Vector(self + -other)

    def __mul__(self, other):

        if isinstance(other, numbers.Real):
            return Vector(other * x for x in self)

        elif isinstance(other, collections.abc.Iterable):
            return Vector(i*j for i, j in it.zip_longest(self, other, fillvalue=1))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return Vector(self * other)

    # @functools.cached_property
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, item):
        cls = type(self)

        if isinstance(item, slice):
            return cls(self.items[item])

        if isinstance(item, int):
            return self.items[item]

        msg = '{cls.__name__} indices must be integers'
        raise TypeError(msg.format(cls=cls))

    def __setitem__(self, key, value):
        self.items[key] = value

    def __getattr__(self, item):
        if len(item) == 1 and 0 <= self.coordinates.find(item) < len(self):
            return self[self.coordinates.find(item)]
        raise AttributeError(f'{type(self).__name__ !r} object has no attribute {item}')

    def __setattr__(self, key, value):
        if key in self.coordinates:
            raise AttributeError(f" can't set {key} attribute to object of {type(self).__name__} class")
        super().__setattr__(key, value)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(i == j for i, j in zip(self, other))
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, initial=1)

    def __reversed__(self):
        self.items = self.items[::-1]
        return self

    def __delitem__(self, key):
        del self.items[key]

    def insert(self, key, value):
        if 0 <= abs(key) < len(self.items):
            a = self.items[:key]
            a.append(value)
            self.items = a + self.items[key:]
            return self.items
        else:
            return self.items.append(value)

    def count(self, item):
        return len([i for i in self if i == item])
