

class Ring:
    #thick = 6

    def __init__(self, radius):
        self._radius = radius
        self.thick = 6
    @property
    def radius(self):
        return ''

    @radius.setter
    def radius(self, val):
        self._radius = val
        return self._radius

    def __getattribute__(self, name):
        if name =='thick':
            return 8
        else:
            return super().__getattribute__(name)

    def __setattr__(self, key, value):
        if '_radius' != key != 'thick':
            print("can't set attribute")
        else:
            super().__setattr__(key, value)
