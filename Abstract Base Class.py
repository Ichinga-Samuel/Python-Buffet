import abc
# abstract base classes ensure that derived class implement some methods of parent class before instantiation


class Base(abc.ABC):
	@abc.abstractmethod
	def foo(self):
		print('foo')
		pass
	
	@abc.abstractmethod
	def bar(self):
		print('bar')
		pass
	
	@abc.abstractmethod
	def boo(self):
		print('boo')
		pass

	def __subclasscheck__(self, subclass):
		if 

class Concrete(Base):
	def foo(self):
		print('foc')
		pass
	
	def fooc(self):
		print('fooc')


print(issubclass(Base, Concrete))   # --> False
con = Concrete()
con.fooc()  # this class won't work unless it correctly implement all the @abstractmethod of the parent class
# this is because Concrete class does not contain the bar method of the Base which is decorated with the @abstractmethod
# Concrete can not function as a derived class of Base unless it implements the two abstract methods of Base