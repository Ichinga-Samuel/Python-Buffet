from concurrent import futures
from flags import save_flag, get_flag, show, main
from time import sleep, strftime, perf_counter
from collections import namedtuple as nt
import os
import random
import functools


MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    pools = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(pools) as executor:
        resp = executor.map(download_one, sorted(cc_list))
    return len(list(resp))


def display(*args):
    print(strftime('[%H:%M:%S]'), end='')
    print(*args)


def loiter(n):
    display(n)
    print(f'loiter({n}):doing nothing for {n}s')
    sleep(n)
    print(f'loiter({n}):done')
    return n*10


def loitering(l):
    display('Start Loitering')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, l)
    display(f'results:{results}')
    display('Waiting for individual Results')
    for i, result in enumerate(results):
        display(f'{i}:{result}')


def compute(a):
    c = random.randint(0, 100)
    display('Starting Counting', a)
    for i in range(c):
        print(f'a = {a} \t c = {i}')
    return a, c


def execute(z):
    executer = futures.ThreadPoolExecutor(max_workers=3)
    res = executer.map(compute, z)
    for i, result in enumerate(res):
        display(f'{i}:{result}')


femscis = nt('Scientists', ['Name', 'Born', 'Field', 'Nobel'])
fems = (femscis('Ada Lovelace', 1815, 'Math', False), femscis('Marie Curie', 1867, 'Physics', True),
        femscis('Ada StarK', '1887', 'Math', False), femscis('Emmy Noether', '1834', 'Math', False),
        femscis('Francisca Noe', '1857', 'Math', False))


def transform(x):
    print(f'{os.getpid()} Processing {x.Name}')
    sleep(1.5)
    res = {'Name': x.Name, 'Age': 2020-x.Born}
    print(f'Done Processing {x.Name}')
    return res


def timer(func):
    @functools.wraps(func)
    def perf(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        print(f'Operation took {perf_counter() - start:.2f} seconds')
        return res
    return perf


@timer
def process():
    with futures.ThreadPoolExecutor() as pool:
        res = pool.map(transform, fems)


