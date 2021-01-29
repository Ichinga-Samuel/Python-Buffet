from functools import partial, wraps


def cor():
    print('Start')
    x = yield
    b = yield x
    d = yield b


def primer(func):
    @wraps(func)
    def prime(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return prime


@primer
def averager():
    total = 0
    count = 1
    average = None

    while True:
        term = yield average
        if term is None:
            break
        count += 1
        total += term
        average = total / count
    return average

