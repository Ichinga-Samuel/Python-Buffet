def nested_property(func):
    ''' nested property documentation '''
    names = func()
    names['doc'] = func.__doc__
    return property(**names)


class Square:
    def __init__(self,value):
        self.sides = value

    @nested_property
    def area():


        def fget(self):
            return self.sides**2


        def fset(self,value):
            print("can't set area ")


        def fdel(self):
            print("can't delete area ")

        return locals()


s=Square(10)
print(s.area)
s.area = 200



