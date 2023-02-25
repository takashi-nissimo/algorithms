"""3-SUM. Given N distinct integers, how many triples sum to exactly zero?"""

from itertools import combinations

from binarysearch import binary_search


class BruteForceThreeSum():
    """Brute-force algorithm for 3-SUM (~ N^3)"""
    @staticmethod
    def print_all(a: list):
        s = '\n'.join(f'{ai} {aj} {ak}'
                      for ai, aj, ak in combinations(a, 3)
                      if ai + aj + ak == 0)
        print(s)

    @staticmethod
    def count(a: list) -> int:
        return sum(1
                   for ai, aj, ak in combinations(a, 3)
                   if ai + aj + ak == 0)


class LinearithmicThreeSum():
    """Sorting-based Linearithmic algorithm for 3-SUM (~ N^2 log N)"""
    @staticmethod
    def print_all(a: list):
        a.sort()
        s = '\n'.join(f'{ai} {aj} {a[k]}'
                      for ai, aj in combinations(a, 2)
                      if (k := binary_search(a, key=-(ai + aj))) is not None
                      if ai < aj < a[k])
        print(s)

    @staticmethod
    def count(a: list) -> int:
        a.sort()
        return sum(1
                   for ai, aj in combinations(a, 2)
                   if (k := binary_search(a, key=-(ai + aj))) is not None
                   if ai < aj < a[k])


class QuadraticThreeSum():
    """Sorting-based Quadratic algorithm for 3-SUM (~ N^2)"""
    @staticmethod
    def print_all(a: list):
        a.sort()
        l = []
        for i in range((n := len(a)) - 2):
            j, k = i + 1, n - 1
            while j < k:
                if (s := a[i] + a[j] + a[k]) == 0:
                    l.append(f'{a[i]} {a[j]} {a[k]}')
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        print('\n'.join(l))

    @staticmethod
    def count(a: list) -> int:
        a.sort()
        c = 0
        for i in range((n := len(a)) - 2):
            j, k = i + 1, n - 1
            while j < k:
                if (s := a[i] + a[j] + a[k]) == 0:
                    c += 1
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return c


if __name__ == '__main__':
    from time import time
    from random import sample

    def print_results(threesum, a):
        t0 = time()
        c = threesum.count(a)
        t = time() - t0
        print(f'{threesum.__name__}\tcount: {c}\ttime: {t}')

    a = sample(range(-1000, 1000), k=400)
    print(f'{len(a) = }')
    # QuadraticThreeSum.print_all(a)
    print_results(BruteForceThreeSum, a)
    print_results(LinearithmicThreeSum, a)
    print_results(QuadraticThreeSum, a)
