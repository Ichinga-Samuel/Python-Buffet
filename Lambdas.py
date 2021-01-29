# lambdas are single expressions used in declaring
a = lambda x, y, d: x * 6 - d + y*d -x
ans = a(3,5,8)
print(ans)  # --> 47
print((lambda x, y, d: x * 6 - d + y*d - x)(3, 5, 8))   # --> 47

# Lambdas can be used as lexical closures in other functions


def adder(n):
	return lambda x: x + n       # uses n from outer scope


add4 = adder(4)
print(add4(7))   # --> 11

