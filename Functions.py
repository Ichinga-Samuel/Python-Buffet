# python functions are first class objects and can be manipulated like other objects.


def yell(t):
	return t.upper() + '!'


bar = yell('woof')  # here the yell function gets executed and the return value is passed to bark
print(bar)  # --> WOOF!

bark = yell  # here the function object that yell points to now has a second name that can be used to call it
bark('woof')  # --> WOOF!

# python objects and there names are separate. if you delete yell the object can still be called with bark
del yell  # deletes the function name yell but
# print(yell('woof'))  # --> NameError: name 'yell' is not defined

bark('woof')  # --> WOOF! bark still exist
s = bark.__name__  # --> yell . yell still remains the function name

# function can be stored in data structures

functions = [bark, str.lower, str.title]
for func in functions:
	print(func, func('hey jude'))


# functions can accept other functions as input
def greet(func, h):
	""" This is a higher order function it accepts functions as argument """
	g = func(h)
	return g


print(greet(bark, 'hi'))
print(greet.__doc__)


def speaker(r):
	def sil(t):     # NESTED OR INNER FUNCTION
		return t.lower()
	return sil(r)


print(speaker('ASSJN'))  # --> assjn

# FUNCTIONS THAT RETURN OTHER FUNCTIONS
def volcon(vol):
	def yell(text):
		return text.upper()
	
	def sil(t):
		return t.lower()
	
	if vol > 5:
		return yell     # return the function object yell
	else:
		return sil
		

fun = volcon(6)
print(fun)  # --> function volcon.<locals>.yell at 0x000001FE5E6F6400>
print(fun('high'))  # --> HIGH

fun = volcon(3)
print(fun)  # --> <function volcon.<locals>.sil at 0x000001FE5E6F6510>
print(fun('HIGH'))  # --> high


# lexical closures are functions that remember values from the enclosing lexical scope even when it is out of scope
def multi(x):
	def mul(y):
		return x * y  # mul remembers x from outer scope
	return mul


m3 = multi(3) # this passes the inner function mul to m3 with the value of x passed on to it
print(m3(5))  # --> 15

# Making objects callable
# to make an object callable the class must have the dunder method __call__


class Multi:
	def __init__(self, n):
		self.n = n
	
	def __call__(self, x):
		return self.n * x  # any object of this class can now make use of this method using open parenthesis and the x arg


m3 = Multi(5)
print(m3(3))  # --> 15

# to check if an object is callable
print(callable(m3))     # --> True
print(callable(bar))    # --> False
print(callable(bark))   # --> True


# unpacking an iterable as a function argument
def abc(a, b, c):
	return a * b * c


al = [4, 5, 6]
print(abc(*al))                     # use * to unpack all iterables apart from dictionaries
aw = {'a': 4, 'b': 5, 'c': 6}       # the keys must match with function variables name
print(abc(**aw))                    # use ** to unpack dictionaries


def func(a, b, *, c):
    """ c is a required keyword argument even if it does not have a default value
		it must be provided in keyword format"""
    return a * b * c


# print(func(2, 3, 4))  # TypeError: func() takes 2 positional arguments but 3 were given
print(func(2, 3, c=4))  # --> 24


def fun(a, b, *, d=3, c):
    """ if there is a default keyword argument it can not be provided in the positional style
        even if it comes before the required keyword argument"""
    return a * b * c * d


print(fun(1, 2, c=3, d=5))


def fun1(a, b, d=3, *, c, **kwargs):
    """ if the * comes after the default keyword argument then the default keyword argument
        can come as a positional argument double ** stands for multiple optional keyword arguments.
        they can be passed in as a dictionary"""
    for i in kwargs.items():
        print(i)
    return a*b*c*d


print(fun1(1, 2, 3, c=4, r=5, t=6, m=9))