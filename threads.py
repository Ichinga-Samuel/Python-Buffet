import time
from threading import Thread, Event


def countdown(n, event):
    while n:
        event.set()
        print(n)
        time.sleep(1.5)
        n -= 1


event = Event()
t = Thread(target=countdown, args=(100, event))


class CountDown:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        m = 0
        while self._running and n:
            print(f'{n} seconds remaining')
            time.sleep(2)
            m += 2
            print(f'{m} seconds gone')
            n -= 1


cd = CountDown()
f = Thread(target=cd.run, args=(20,))
