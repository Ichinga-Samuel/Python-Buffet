from string import Template


# String Formatting Using The % Operator
regno = 25689
name = 'Bob'
errno = 50159747054

print('hello %s' % name)  # this returns --> hello Bob
print('hello %s your regno is %d' % (name, regno))  # --> hello Bob your regno is 25689
# if making more than one sub put them in a tuple and put the operator outside it like this %(sub1, sub2)

# convert to hexadecimal
print('%d in hexadecimal is %x' % (errno, errno))  # --> 50159747054 in hexadecimal is badc0ffee

# another crazy style that helps you ignore order using keywords
print('hey %(n)s you have a %(e)x' % {'e': errno, 'n': name})  # --> hey Bob you have a badc0ffee

# String Formatting Using The String Format Method
# when using numbers to indicate a position start with zero and increase accordingly
print('my name is {0} I am {1} years old'.format('Samuel', 24))  # --> my name is Samuel I am 24 years old

# Using empty braces. Put the arguments in the format method as you want them to appear.
print('my name is {} I am {} years old'.format('Samuel', 24))  # --> my name is Samuel I am 24 years old

# using keywords. when using keywords arguments in the format method can be in any other
print('my name is {name} I am {age} years old'.format(name='Samuel', age=24))  # --> my name is Samuel I am 24 years old

# Arguments can be literals or variables and you can mix positional with keywords
#  as long as all the positional comes first
print('my name is {} I am {age} years old'.format(name, age=24))  # --> my name is Bob I am 24 years old

# Format specifier.
# Format specifiers come in this order.  [fill][align][sign][#][0][width][,][.precision][type]
# Fill. this can be any character other than '{' or '}'

# Align includes the following
# '<' which forces the field character to be left aligned within the available space
# '>' which forces the field character to be right aligned within the available space
# '=' this forces padding to be placed after the sign before the digits. only for numeric use e.g. +234
# '^' forces the field character to be centered within the available space
# the number after the sign indicates the available space

print('this is left {:<10} and this is right {:>10} while this is center {:^10} alongside this {:=+10}'.format(10, 10, 10, +17))


# Sign includes the following
# '+' indicates that a sign should be used for both negative and positive numbers
# '-' indicates that a minus sign should be used for negative numbers but none for positive numbers
# ' ' empty space indicates that a space should be use for positive numbers and minus sign for positive numbers
print('show the signs for this {:+} and {:+} but use space for this {: } and this {: } the default is {:-} and this'
	  ' {:-} but let us try this {} and this {}'.format(2, -2, 2, -2, 2, -2, 2, -2))


# "#" is used for number conversion
# 'b' is for binary conversion
# 'o' is for octal conversion
# 'c' is for character conversion. it converts an integer to the corresponding unicode character
# 'd' is for decimal conversion
# 'x' is for hexadecimal conversion with small letters
# 'X' is for hexadecimal conversion with big letters
# 'n' same as d but uses locale default to choose separator
# 'e' prints number in scientific notation using 'e'
# 'E' prints number in scientific notation using 'E'
# 'f' and 'F' displays the number as fixed point display 'F' displays inf, nan as INF, NAN
# 'G' and 'g' this is the general formats. displays number according to level of precision indicated and uses 'e' or 'E' when necessary
# '%' multiplies the number by 100

#print(f'{:^10NUMBER CONVERSIONS}')

a = 344
b = 200
print('the number is {0:>5b}, {0:o}, {1:c}, {0:d}, {0:x}, {0:X}, {0:n}'.format(a, b))
# this returns --> the number is 1101001001001110101110, 15111656, È, 3445678, 3493ae, 3493AE, 3445678

# accessing an objects attributes
num = 3-4j
print('{0} is complex number {0.real} is the real part and {0.imag} is the imaginary part'.format(num))
print('{c} is complex number {c.real} is the real part and {c.imag} is the imaginary part'.format(c=num))


class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y
	
	def __str__(self):
		return 'Point({self.x}, {self.y})'.format(self=self)


v = Point(3,4)
print('the point is {!rc}.the x cord is {c.x} and the y cord is {c.y}'.format(c=v))

# accessing object items
a = ['amaka', 'chioma', 'obi']
b = {'one': 'otu', 'two': 'abuo'}

print("the numbers are {0[one]}, and {0[two]} represented in {0}".format(b))
# the output --> the numbers are otu, and abuo represented in {'one': 'otu', 'two': 'abuo'}
print('these are the names {0[1]} and {0[2]}'.format(a))
# the output --> these are the names chioma and obi

print('i am {:1%} percent per sure'.format(1))
# --> i am 100.000000% percent per sure

# using * and ** to unpack list and dictionary with using indexing
c = [8, 9, 13, 48, 57]
print('{0:b} {0:b} {0:b} {0:b} {0:b}'.format(*c))
# --> 1000 1000 1000 1000 1000
print('there names are {}, {}'.format(*b))
# --> there names are one, two

# using !r and !s for repr() and str() respectively
print("repr() shows {!r} but str() don't show {!s}".format('quotes', 'quotes'))  # --> repr() shows 'quotes' but str() don't show quotes


# Template Strings
# use template strings for user supplied strings for security reasons.
s = Template('$who likes $what')  # place dollar sign $ beside the word you wish to substitute
sub = s.substitute(who='sam', what='python')
print(sub) # --> sam likes python
# a dictionary can also be used to make substitution
d = {'who': 'Ichinga', 'what': 'Programming'}
dsub = s.substitute(d)
print(dsub)  # --> Ichinga likes Programming

# using safe_substitute. This prevents error if there is no placeholder
safe = s.safe_substitute(who='sam')  # no placeholder for what
print(safe)  # no error despite missing placeholder --> sam likes $what


# if all variables

# when using safe_substitute