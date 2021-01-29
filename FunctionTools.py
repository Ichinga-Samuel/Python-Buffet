import operator as op
from functools import *
from collections import namedtuple as nt

class example:

    def __init__(self, start):
        self.start = start
        self.array = list(range(1, start))

    @lru_cache(maxsize=32)
    def mean(self):
        return sum(self.array)/len(self.array)


s = example(10)
s.mean()  # --> 10.0
s.mean()
s.mean()
s.mean()
s.mean.cache_info()  # --> CacheInfo(hits=3, misses=1, maxsize=32, currsize=1)
s.mean.cache_clear()


def anom(b, c):
    return f'X is {b+c} years old'


@singledispatch
def fun(a, b, c):
    return f'Mr {a} is {b+c} years old'


@fun.register
def fun_string(a: str, b, c):
    return f'Mrs {a} is {b+c} years old'


@fun.register(int)
def fun_int(a, b, c):
    return f'He is {a+b+c} years old'


fun.register(float, anom)

array = list(range(4, 79, 3))
getter = op.itemgetter(2, 7)
getter(array)
dic = {'1': 'man', 2: 'woman', '3': 'girl', 4: 'boy'}
dgetter = op.itemgetter(2, '3', '1')
dgetter(dic)

P = nt('Point', 'x y z')
p = P(2, 4, 6)
at = getattr(p, 'x')
atr = op.attrgetter('x', 'y')
atr(p)