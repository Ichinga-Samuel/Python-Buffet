from math import atan2, hypot, sqrt


class Repeater:
    def __init__(self, value, max_repeat=5):
        self.value = value
        self.count = 0
        self.max_repeat = max_repeat

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeat:
            raise StopIteration('Exceeded Amount')
        self.count += 1
        return self.value


val = Repeater('Samuel', 7)


class Vector2D:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __len__(self):
        return len((self.x, self.y))

    def __getitem__(self, i):
        sq = list(self)
        return sq[i]

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x !r}, {self.y !r})'

    def __str__(self):
        return f'{tuple(self)}'

    def __format__(self, spec=''):
        if spec.endswith('p'):
            spec = spec[:-1]
            cord = (abs(self), self.angle())
            output = '<{}, {}>'
        else:
            cord = self
            output = '{}, {}'

        comp = (format(i, spec) for i in cord)
        return output.format(*comp)

    def __abs__(self):
        return hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __byrtes__(self):
        return bytearray(self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def angle(self):
        return atan2(self.y, self.x)


v = Vector2D(2, 3)
len(v)


class CountDown1:

    def __init__(self, start):
        self.x = start

    def __iter__(self):
        return CountDownIter(self.x)


class CountDownIter:

    def __init__(self, count):
        self.c = count

    def __next__(self):
        if self.c == 0:
            raise StopIteration('Start')
        self.c -= 1
        return self.c


class Countdown:

    def __init__(self, start):
        self.s = start

    def __iter__(self):
        return iter(range(self.s, 0, -1))


