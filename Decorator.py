from functools import wraps, partial
import pickle


# Using decorators to check argument type and number of arguments
def check(func=None, *, dt='', n=0):
    """ A Decorator function that checks if the arguments are of the correct type an the right amount
        n: --> number of arguments
        dt: --> Data types of the arguments
    """
    if func is None:
        return partial(check, dt=dt, n=n)

    @wraps(func)
    def checker(*args, **kwargs):
        if (len(args) + len(kwargs)) != n:
            raise ValueError('Incomplete number of arguments')

        else:
            for arg, argtype in zip(args, dt):
                if type(arg) != argtype:
                    err = f'expected {argtype} got {type(arg)}'
                    raise ValueError('Wrong Object Type ' + err)

            else:
                print('Arguments Correct Proceeding With Computations')
                return func(*args, **kwargs)
    return checker


# Using Decorators For Caching
def cache(func):
    """ A Decorator For Caching """
    cached = {}

    @wraps(func)
    def _cache(*args, **kwargs):
        key = pickle.dumps((args, kwargs))  # creates a Key using the positional and keyword arguments
        if key not in cached:
            print('Computing For the First Time')
            cached[key] = func(*args, **kwargs)
        else:
            print('Retrieving From Cache')
        return cached[key]
    return _cache


@cache
@check(dt=[int, float], n=2)
def add(a, b):
    return a + b


print(add(5, 7.0))  # ---> Computing For the First Time
#                          Arguments Correct Proceeding With Computations
#                          12.0

# computing again with the same arguments
print(add(5, 7.0))  # --->  Retrieving From Cache
#                           12.0

# Other Uses of Decorators are
# Logging
# Timing
# Verification
# Registration
