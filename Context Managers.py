from time import perf_counter
import contextlib


class Indenter:

    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 4

    def printi(self, txt):
        print(' '*self.level+txt)


@contextlib.contextmanager
def timmit(label):
    start = perf_counter()
    try:
        yield
    finally:
        end = perf_counter()
        print(f'This {label} operation took {end - start}nano seconds')


with Indenter() as indent:
    indent.printi('hello')
    with indent:
        indent.printi('hi')
        with indent:
            indent.printi('hey')
        indent.printi('hi')
    indent.printi('hello')

with timmit('count to 100000'):
    i = 0
    while i < 100000:
        i += 1
