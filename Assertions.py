def apply_discount(product, discount):
	price = int(product['price'] * (1.0 - discount))
	
	# This asserts that the discount can't be lower than zero and the new price can't be higher than the original
	# The part in single quotes will be printed when assertion fails and AssertionError arises
	assert 0 <= price <= product['price'], 'Must be less than original price'
	return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes, 2))

# Don't use assert for data validation.
# it can be globally disabled with the -0 and -00 command line switches as well as PYTHONOPTIMIZE environment variable
# in cpython. This turns the assert statement into a null operation that won't be evaluated

# Never try to assert a tuple, it will always return True
# don't do this assert (x==10, 'x should be equal to 10)
