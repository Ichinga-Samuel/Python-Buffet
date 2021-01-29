import random
import time


def simulate(a, b,i):
    A = a
    B = b
    PA = i * (A)/(A/B)
    PB = i-1
    k = a + b
    round = 0
    while A < k and A != 0 and 000:
        round += 1
        print(f'Round {round}!')
        p = random.random()
        if p <= i:
            A += 10
            B -= 10
        else:
            B += 10
            A -= 10
        print(f'Player A has {A} and Player B has {B}')
        # time.sleep(0.5)

    if A == k:
        winner = 'A'
    elif B == k:
        winner = 'B'
    else:
        print(f'No winner after {round} rounds')
        return

    print(f'Game Over after {round} rounds Player {winner} has won the Jackpot!')