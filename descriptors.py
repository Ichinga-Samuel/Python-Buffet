import types
from functools import wraps


class NonNeg(metaclass=):
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 0:
            raise AttributeError('Negative Number Not Supported')
        instance.__dict__[self.name] = value


class Descriptors:
    @staticmethod
    def non_neg(cls):
        super_set = cls.__setattr__

        def __set__(self, instance, value):
            if value < 0:
                raise ValueError('Negative Number Not Supported')
            super_set(self, instance, value)
        cls.__setattr__ = __set__
        return cls

    @staticmethod
    def Typed(expected_type, cls=None):
        if cls is None:
            return lambda cls: Descriptors.Typed(expected_type, cls)

        super_set = cls.__setattr__

        def __set__(self, instance, value):
            if not isinstance(value, expected_type):
                raise TypeError('expected ' + str(expected_type))
            super_set(self, instance, value)
        cls.__setattr__ = __set__
        return cls

    @staticmethod
    def readonly(cls):

        def __set__(self, instance, value):
            raise AttributeError

        cls.__set__ = __set__

        def __get__(self, instance, owner):
            return

        return cls


class Stock:
    price = NonNeg('price')
    order = NonNeg('order')

    def __init__(self, price, order):
        self.price = price
        self.order = order


@Descriptors.Typed(int)
@Descriptors.non_neg
@Descriptors.readonly
class Goods:
    def __init__(self, price, order):
        self.price = price
        self.order = order


class Profile:

    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


s = Stock(3, 9)
g = Goods(56, 9)
