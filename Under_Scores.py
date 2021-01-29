# Underscores has many meanings in python both conventional and interpreter enforced

							# single leading underscore _var
# this is conventional and not interpreter enforced it indicates that a variable is intended for private or internal use
# it tells other programmers not to tamper with this variable. if part of a module using the wildcard * to import all
# will not import this variable unless an __all__ variable is implemented in this module.

							# trailing underscore var_
# this is used by convention to avoid clash  with python keywords
class_ = 'avoid clash with python key word class'

							# double leading underscore(dunders)  __var
# This is enforced by the interpreter in a process known as name mangling. it prevents a subclass from overriding a
# variable in the super class. a variable with two leading underscores is renamed to something like this _classname__var


class Test:
	def __init__(self):
		self.__name = 'hey'


# the dir of this class won't show a variable named __name
t = Test()
print(t._Test__name)

