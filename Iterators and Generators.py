
lis = iter(range(0, 25, 5))  # iter() makes an object into an iterator object which can be passed to next() function
a = next(lis)
b = next(lis)
print(lis)  # --> range_iterator object at 0x0000024CA58F6730>
print(a)    # --> 0
print(b)    # --> 5

try:
    for i in lis:
        print(next(lis))
except StopIteration as err:
    print(err, 'We have come to the End')

# --> 0, 5, 15
# at the end of iterator a StopIteration exception is thrown


# Generators
# a generator is just a function that has yield statement in it
def gen(v, bi, e):
    for va in range(bi, v, e):
        yield(va)


genn = gen(33, 3, 9)
print(genn)            # --> <generator object gen at 0x0000026A3BB30B30>
print(next(genn))      # --> 3
# generator objects also throw up StopIteration exceptions at the end of generator
# there are generator comprehensions just like list comprehensions but enclosed in brackets

gencomp = (i for i in range(100))
print(gencomp)  # --> <generator object <genexpr> at 0x0000023EC81BCAC0>
print(next(gencomp))  # --> 0

# Co-Routines
# The yield statement can also receive values which can be sent to the generator


def show_upper():
    # create a loop
    while True:
        text = yield
        print(text.upper())
        # return text.upper()   using return will throw up a StopIteration exception


co = show_upper()
print(co)  # --> generator object show_upper at 0x000002214267CAC0>
next(co)   # to kick start the co-routine use next() first before sending to the generator
co.send('Hello')   # --> HELLO
co.send('samuel')  # --> SAMUEL

# use decorator to avoid having to call next() first
def decgen(func):

    def _decgen(*args, **kwargs):
        ngen = func(*args, **kwargs)
        next(ngen)
        # next() has been called on the generator object so it will be returned instead of the generator function
        return ngen
    return _decgen


@decgen
def show_upper():
    # giving the co-routine a return value
    result = None
    while True:
        text = yield result
        result = text.upper()
        print(result)


cor = show_upper()
# no need for next(cor)
a = cor.send('amen')  # -->  Amen
print(a)
b = cor.send('sam')
print(b)

# closing a co-routine and passing arguments it
cor.close()
# cor.send('hi')   # --> StopIteration
# after closure GeneratorExit exception is thrown using send again will throw a StopIteration exception


@decgen
def coroute(num):
    while True:
        value = yield
        if value % num == 0:
            print(value * 2)


even = coroute(2)
even.send(8)  # -->
even.send(60)
ab = even.send(6)
print(ab)
