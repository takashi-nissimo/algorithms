"""Search in a bitonic array.
An array is bitonic if it is comprised of an increasing sequence of integers
followed immediately by a decreasing sequence of integers.
Write a program that, given a bitonic array of n distinct integer values,
determines whether a given integer is in the array.
"""

from typing import Union

from binarysearch import binary_search


def search_bitonic_peak(a: list) -> int:
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > a[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_bitonic(a: list, key: int) -> Union[int, None]:
    peak = search_bitonic_peak(a)
    if key > a[peak]:
        return None
    elif key == a[peak]:
        return peak
    else:
        if (idx := binary_search(a[:peak], key, descend=False)) is not None:
            return idx
        if (idx := binary_search(a[peak+1:], key, descend=True)) is not None:
            return idx + peak + 1


if __name__ == '__main__':
    from sys import argv
    from random import randrange
    from time import time
    from statistics import mean
    
    def calc_worst_time(n: int, verbose: bool = False) -> float:
        p = randrange(1, n)
        a = list(range(-p, p, 2)) + list(reversed(range(p-n+1, n-p+1, 2)))
        
        t_max = 0.
        for key in a:
            t0 = time()
            idx = search_bitonic(a, key)
            t = time() - t0
            t_max = max(t_max, t)
            if verbose:
                print(f'{key = }, {idx = }, time = {t}')
        if verbose:
            print(f'{a = }\nworst time: {t_max}')
        return t_max

    n, trials = int(argv[1]), int(argv[2])
    mean_worst_time = mean(calc_worst_time(n) for _ in range(trials))
    print(f'{n = }, {trials = }, {mean_worst_time = }')
