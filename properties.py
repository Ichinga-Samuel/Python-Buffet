from functools import cached_property


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = -value

    x = property(fget=getx, fset=setx, fdel=None, doc='')


p = Point(3, 5, 7)


class Range:
    step = 8
    end = 9

    def __init__(self, start, stop, step):
        self.stop = stop
        self.step = step
        self.start = start

    def __setattr__(self, key, value):
        if key == 'rsum' or key not in ['stop', 'step', 'start']:
            pass
        else:
            super().__setattr__(key, value)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        if value > self.stop:
            self.__start, self.stop = self.stop, value
        else:
            self.__start = value

    @cached_property
    def rsum(self):
        return sum(range(self.start, self.stop))


r = Range(2, 8, 3)
