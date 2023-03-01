"""Egg drop.
Suppose that you have an n-story building (with floors 1 through n)
and plenty of eggs. An egg breaks if it is dropped from floor T or higher
and does not break otherwise. Your goal is to devise a strategy to determine
the value of T given the following limitations on the number of eggs and tosses:
    - Version 0: 1 egg, <= T tosses.
    - Version 1: ~ 1*lg(n) eggs and ~ 1*lg(n) tosses.
    - Version 2: ~ lg(T) eggs end ~ 2*lg(n) tosses.
    - Version 3: 2 eggs and ~ 2*sqrt(n) tosses.
    - Version 4: 2 eggs and <= c*sqrt(T) tosses for some fixed constant c.
"""

from __future__ import annotations  # for python<3.9
from abc import ABCMeta, abstractmethod
from math import sqrt, ceil
from statistics import mean


class EggDrop(metaclass=ABCMeta):
    """Abstract Class for Egg drop."""

    def __init__(self, b: list[bool]):
        self.n_egg = 1
        self.n_toss = 0
        self.b = b

    @abstractmethod
    def findT(self) -> int:
        pass


class EggDropV0(EggDrop):
    """Egg drop. Version 0: 1 egg, <= T tosses."""

    def __init__(self, b: list[bool]):
        super().__init__(b)

    def findT(self) -> int:
        for i, bi in enumerate(self.b):
            self.n_toss += 1
            if bi:
                return i + 1


class EggDropV1(EggDrop):
    """Egg drop. Version 1: ~ 1*lg(n) eggs and ~ 1*lg(n) tosses."""

    def __init__(self, b: list[bool]):
        super().__init__(b)

    def findT(self) -> int:
        lo, hi = 0, len(self.b) - 1
        while lo <= hi:
            self.n_toss += 1
            mid = lo + (hi - lo) // 2
            if self.b[mid]:
                self.n_egg += 1
                hi = mid - 1
            else:
                lo = mid + 1
        return lo + 1


class EggDropV2(EggDrop):
    """Egg drop. Version 2: ~ lg(T) eggs end ~ 2*lg(n) tosses."""

    def __init__(self, b: list[bool]):
        super().__init__(b)

    def findT(self) -> int:
        top = len(self.b) - 1
        i = 1
        while True:
            j = 1
            while True:
                self.n_toss += 1
                if self.b[(idx := min(i + j - 2, top))]:
                    if j == 1:
                        return idx + 1
                    self.n_egg += 1
                    break
                j *= 2
            i += j // 2


class EggDropV3(EggDrop):
    """Egg drop. Version 3: 2 eggs and ~ 2*sqrt(n) tosses."""

    def __init__(self, b: list[bool]):
        super().__init__(b)

    def findT(self) -> int:
        i = 0
        j = ceil(sqrt(n := len(self.b)))
        while True:
            i += j
            self.n_toss += 1
            if self.b[min(i, n - 1)]:
                self.n_egg += 1
                break
        for j in range(i - j, i):
            self.n_toss += 1
            if self.b[j]:
                return j + 1
        return j + 2


class EggDropV4(EggDrop):
    """Egg drop. 
        Version 4: 2 eggs and <= c*sqrt(T) tosses for some fixed constant c."""

    def __init__(self, b: list[bool]):
        super().__init__(b)

    def findT(self) -> int:
        i = 0
        j = ceil(sqrt(2 * (n := len(self.b))))
        while True:
            i += j
            j -= 1
            self.n_toss += 1
            if self.b[min(i, n - 1)]:
                self.n_egg += 1
                break
        for j in range(i - j - 1, i):
            self.n_toss += 1
            if self.b[j]:
                return j + 1
        return j + 2


class EggDropStats():
    """Stats class for Egg-drop."""

    def __init__(self, eggdrop: EggDrop, n: int):
        self.n = n
        self.method = eggdrop.__name__
        self.eggs = []
        self.tosses = []
        for i in range(n):
            b = [False] * i + [True] * (n - i)
            ed = eggdrop(b)
            if (T := ed.findT()) != i + 1:
                raise Exception(f'{T} != {i + 1}')
            self.eggs.append(ed.n_egg)
            self.tosses.append(ed.n_toss)

    def print(self):
        print(',\t'.join([
            self.method,
            f'n: {self.n}',
            f'mean eggs: {mean(self.eggs):.3f}',
            f'max eggs: {max(self.eggs)}',
            f'mean tosses: {mean(self.tosses):3.3f}',
            f'max tosses: {max(self.tosses)}',
        ]))


if __name__ == '__main__':
    from sys import argv
    n = int(argv[1])
    EggDropStats(EggDropV0, n).print()
    EggDropStats(EggDropV1, n).print()
    EggDropStats(EggDropV2, n).print()
    EggDropStats(EggDropV3, n).print()
    EggDropStats(EggDropV4, n).print()
