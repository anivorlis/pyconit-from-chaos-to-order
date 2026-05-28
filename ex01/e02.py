# But.. Is the dice really fair? Let's do some statistics!
# We will use scipy for that, but you can also do it with the standard library if you want to.

import numpy as np

from ex01.e01 import roll_dice


def dice_simulation(N):
    '''Simulate rolling a fair dice N times and return the results as a numpy array.'''
    return np.fromiter((roll_dice() for _ in range(N)), dtype=np.int8, count=N)


def dice_statistics(results):
    '''Count how many times each face (1..6) was rolled.'''
    counts = np.bincount(results, minlength=7)[1:]
    return dict(zip(range(1, 7), counts.tolist()))


if __name__ == '__main__':
    results = dice_simulation(1000)
    stats = dice_statistics(results)
    print(stats)


