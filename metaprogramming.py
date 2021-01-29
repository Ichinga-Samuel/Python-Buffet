import weakref


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class New(metaclass=Singleton):

    def __init__(self, value):
        self.value = value


class Cached(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        if args in cls._cache:
            print('retriving from cache')
            return cls._cache[args]
        else:
            obj = super().__call__(*args)
            cls._cache[args] = obj
            return obj


class Shape(metaclass=Cached):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.breadth * self.length


class MyMeta(type):
    # A meta class that takes extra arguments
    @classmethod
    def __prepare__(mcs, name, bases, *, debug=True, type_ = int):
        # custom processing
        return super().__prepare__(name, bases)

    def __new__(mcs, name, bases, ns, *, debug=True, type_ = int):
        return super().__new__(mcs, name, bases, ns)

    def __init__(mcs, name, bases, ns, *, debug=True, type_ = int):
        return super().__init__(name, bses, ns)
