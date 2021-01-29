import time
from threading import Thread


def factorize(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i


def run_factorize(numbers):
    start = time.perf_counter()
    fact = []
    [factor_list(n, fact) for n in numbers]
    end = time.perf_counter()
    print(f'Took {end-start:.3f} seconds')
    return fact


def factor(number, name):
    with open(f'{name}.txt', 'a') as ft:
        fact = list(factorize(number))
        ft.write(f'{number}: {fact}\n')


def factor_list(number, lis=[]):
    fact = list(factorize(number))
    lis.append(fact)


def thread_factorize(numbers):
    facts = []
    start = time.perf_counter()
    threads = []
    for number in numbers:
        t = Thread(target=factor_list, args=(number, facts))
        t.start()
        threads.append(t)

    [thread.join() for thread in threads]
    end = time.perf_counter()
    print(f'Took {end-start:.3f} seconds')
    return facts


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = factor(self.number)
        return self.factors


def thread_class(numbers):
    start = time.time()
    threads = []
    ff = []
    for number in numbers:
        t = FactorizeThread(number)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    end = time.time()
    print(f'Took {end-start:.3f} seconds')


class Counter:
    def __init__(self):
        self.count = 0

    def increase(self, num):
        self.count += num


def worker(index, amount, counter):
    counter.increase(amount)


def thread_counter():
    s = time.perf_counter()
    a = 10**5
    counter = Counter()
    threads = []
    for i in range(5):
        t = Thread(target=worker, args=(i, a, counter))
        t.start()
        threads.append(t)
    [thread.join() for thread in threads]
    e = time.perf_counter()
    print(f'Expected {500000} but got {counter.count}. It took {e-s:.3f} secs')


numbers = [2139079, 1214759, 1516637, 1852285]




