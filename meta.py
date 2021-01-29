import json
from collections import abc


with open('data.json') as jd:
    pd = json.load(jd)


class DotAccess:

    def __init__(self, data):
        self.data = dict(data)

    def __getattr__(self, item):
        if hasattr(self.data, item):
            return getattr(self.data, item)
        else:
            return DotAccess.dot(self.data[item])

    @classmethod
    def dot(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.dot(i) for i in obj]
        else:
            return obj


# Using __new__


class DotAccess2:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(i) for i in arg]
        else:
            return arg

        def __init__(self, data):
            self.data = dict(data)

        def __getattr__(self, item):
            if hasattr(self.data, item):
                return getattr(self.data, item)
            else:
                return DotAccess2(self.data[item])


print(pd)
p = DotAccess2(pd)
