import functools
# a decorator is a callable that takes another callable as input and returns a callable
# A simple decorator


def null_deco(func):    # null_deco is a callable and the input func is also a callable
	return func         # the same func is also returned


def greet():
	return 'hello'


# using it to wrap or decorate another function manually
g = null_deco(greet)    # greet has been decorated with null_deco
print(g())


# decorating using the @func syntactic sugar
@null_deco
def greet():
	return 'hello'


def upper_case(func):
	def wrapper():
		result = func()
		m_result = result.upper()
		return m_result
	return wrapper


# manually using this decorator on the greet function
decorated_func = upper_case(greet)
print(decorated_func())     # --> HELLO


# using @syntax
@upper_case
def greet():
	return 'hello'


print(greet())      # --> HELLO


def strong(func):
	def wrapper():
		return '<strong> ' + func() + ' </strong>'
	return wrapper


def emphasis(func):
	def wrapper():
		return '<em> ' + func() + ' <em>'
	return wrapper


# using multiple decorators
@upper_case
@strong
@emphasis
def greet():
	return 'hello'


print(greet())      # <STRONG> <EM> HELLO <EM> </STRONG>
# notice the order of execution emphasis decorated first followed by strong and then uppercase


# decorating functions with arguments
def proxy(func):
	def wrapper(*args, **kwargs):  # *args and *kwargs collect all the arguments and keywords arguments
		return func(*args, **kwargs)
	return wrapper


def trace(func):
	def tracer(*args, **kwargs):
		"""this is the docstring of the wrapper trace function """
		print(f'TRACE: calling {func.__name__}()')
		print(f'with {args}, {kwargs}')
		
		result = func(*args, **kwargs)
		
		print(f'TRACE: {func.__name__}()')
		print(f'returned {result!r}')
		return result
	return tracer


@trace
def multi(a, b, c=8):
	""" performs arithmetic operations this is the docstring of multi() """
	return a * b - c


print(multi(4, 5, c=-6))    # --> TRACE: calling multi()
#      						with (4, 5), {'c': -6}
# 	                        TRACE: multi()
# 	                        returned 12
#                       	12

# when using decorators there is exchange of metadata(eg __name__, __doc__)
# information between the decorated function and the inner wrapper function of the decorator
print(multi.__name__)  # --> tracer
print(multi.__doc__)   # --> this is the docstring of the wrapper trace function


# to solve this problem we will use functools.wraps
def trace(func):
	@functools.wraps(func)  # this enables the decorated function to retain its metadata
	def tracer(*args, **kwargs):
		"""this is the docstring of the wrapper trace function """
		print(len(args), len(kwargs))
		print(f'TRACE: calling {func.__name__}()')
		print(f'with {args}, {kwargs}')
		
		result = func(*args, **kwargs)
		
		print(f'TRACE: {func.__name__}()')
		print(f'returned {result!r}')
		return result
	
	return tracer


@trace
def multi(a, b, c=8):
	""" performs arithmetic operations this is the docstring of multi() """
	return a * b - c


print(multi.__name__)  # the correct name no displays --> multi
print(multi.__doc__)    # --> performs arithmetic operations this is the docstring of multi()
multi(5, 10, c=7)
