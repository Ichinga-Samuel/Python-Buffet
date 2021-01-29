def mA():
    total = 0
    avg = 0
    count = 1
    while avg is not None:
        term = yield str(avg)
        total += term
        avg = total / count
        count += 1


def yd():
    b = yield
    print(b,'b')
    c = yield b
    print(c,'c')
    d = yield c
    print(d,'d')
    e = yield d
    print(e, d, 'stop')


def fib():
    a, b = 0, 1
    while True:
        a, b = a+b, a
        yield a


def rfib(n):

    if n<=2:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)