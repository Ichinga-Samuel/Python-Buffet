from functools import wraps, partial
from types import MethodType

# decorators with arguments
# a decorator with arguments can be written with 2 closures


def printname(prefix=''):       # a function to carry the argument passed to be passed to the decorator
	def addprefix(func):        # the main decorator starts here
		msg = prefix + func.__name__

		@wraps(func)
		def pn(*args, **kwargs):
			print(msg)
			return func(*args, **kwargs)
		return pn
	return addprefix


@printname('This is ')
def multi(a, b, c):
	""" performs arithmetic operations this is the docstring of multi() """
	return a * b - c


print(multi(7, 9, 8))  # --> This is multi and returns --> 55


# using partial to remove the third function
def addprefix(func=None, *, pre=''):
	if func is None:
		# The argument passed to a decorator can only be a keyword argument
		# partial is used here because when the decorator is passed with an argument then the decorator will not find the
		# func argument so partial is use to avoid error
		return partial(addprefix, pre=pre)  # the kwarg of the decorator is passed to partial as a kwargs using the same
#    										  name for the  kwarg and it's value

	@wraps(func)
	def pn(*args, **kwargs):
		print(pre + func.__name__)
		print(args)
		return func(*args, **kwargs)
	return pn


@addprefix(pre='Hello ')  # @addPrefix(prefix='') addPrefix must be called with the prefix keyword arguments
def multi(a, b, c):
	""" performs arithmetic operations this is the docstring of multi() """
	return a * b - c


print(multi(7, 9, 5))  # --> Hello multi and returns --> 55


# Decorating a recursive function
# when recursive functions are decorated the decorations keep appearing at each recursive call
# Therefore it is not advisable to decorate recursive Functions
#  @addprefix(pre='Hello ')
def recursive(x):
	if x == 0:
		return x
	else:
		return recursive(x-1) + x


print(recursive(10))  # ---> 55 and print Hello recursive 10 times which is the number of recursive call required


# Decorating a class
# Decorators can be a useful way of adding class variables

def mark(cls):
	cls.added_attr = 'I am a decorated class'  # This will be a class variable
	cls.name = f'My name is {cls.__name__}'		# The decorated class attributes can be accessed
	return cls


def marker(cls=None, *, a=0, b=0):
	if cls is None:
		return partial(marker, a=a, b=b)

	@wraps(cls)
	def _marker(*args, **kwargs):
		c = a * b
		cls.weight = c
		return cls(*args, **kwargs)
	return _marker


# Using Decorators to create singleton classes
# A Singleton class is a class which only one object at a time can be created

def singleton(cls):
	instance = [None]

	@wraps(cls)
	def _singleton(*args, **kwargs):
		if instance[0] is None:
			instance[0] = cls(*args, **kwargs)
		return instance[0]

	return _singleton


@mark
@marker(a=5, b=6)
class Rank:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


general = Rank('Samuel', 'Male')
cop = Rank('Obi', 'Male')
print(Rank.added_attr)  # ---> I am a decorated class
print(Rank.name)
print(cop.name)		# ---> Obi
print(general.weight)   # ---> 30
print(general.name)		# ---> Samuel


@singleton
class Ranks:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


man = Ranks('Adam', 'Male')
woman = Ranks('Eve', 'Female')
print(man.name)   # ---> Adam
print(woman.name)  # --->  also prints Adam because only one instance can be created


# Class Decorators
class Decorator:
	""" A Decorator Class """

	def __init__(self, func):
		self.func = wraps(func)

	def __call__(self, *args, **kwargs):  # A Decorator class must have a __call__ method
		print('Before Decorating')
		res = self.func(*args, **kwargs)
		print(res)
		print('After Decorating')
		return res

	def __get__(self, instance, cls):  # To decorate a method a class must implement a __get__ method
		# The __get__ method returns a method if it is called on an instance
		return self if instance is None else MethodType(self, instance)


class DecoratedClass:
	""" A Class Decorated by Decorator Class"""
	def __init__(self, ab, ba):
		self.a = ab
		self.b = ba

	@Decorator
	def adder(self):
		return self.a + self.b


a = DecoratedClass(10, 23)
a.adder()
print(type(a))

@Decorator
def multi(q, r):
	""" Multiplies Two Numbers"""
	aq = q * r
	return aq


print(type(multi))  # ---> <class '__main__.Decorator'>
print(multi.__doc__)


