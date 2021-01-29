import multiprocessing as mp
import time


def is_prime(n):
    if n in (2, 3):
        print(True)
        return True
    if n % 2 or n % 5 == 0:
        print(False)
        return False
    stop = round(n**0.5) + 1
    for divisor in range(3, stop, 2):
        if n % divisor == 0:
            print(False)
            return False
    print(True)
    return True


def factorize(n):
    stop = round(n/2) + 1
    for i in range(1, stop):
        if n % i == 0:
            yield i


def r_factorize(n):
    stop = round(n / 2) + 1
    result = []
    for i in range(1, stop):
        if n % i == 0:
            result.append(i)
    return result


def add(a, b, c=6, n=7):
    return a + b + c + n


def timer(func, args=(), kwargs={}):
    start = time.perf_counter()
    func(*args, **kwargs)
    print(f'It took {time.perf_counter()-start} seconds')


if __name__ == '__main__':
    primes = [2344, 567, 867679, 657544, 35235353, 46646, 536266]
    values = [(4, 5), (6, 8), (9, 2)]
    pool = mp.Pool(processes=2, maxtasksperchild=1)
    result = pool.apply_async(r_factorize, (25, ))
    m = pool.map(r_factorize, primes)
    g = pool.imap(r_factorize, primes)
    s = pool.starmap(add, values)
    r = pool.imap_unordered(factorize, (789, ))
    print(result.get())
