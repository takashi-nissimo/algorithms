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


class EggDrop(metaclass=ABCMeta):
    """Abstract Class for Egg drop."""
    def __init__(self, break_flags: list[bool]):
        self.n_egg = 1
        self.n_toss = 0
        self.bs = break_flags

    @abstractmethod
    def findT(self) -> int:
        pass


class EggDropV0(EggDrop):
    """Egg drop. Version 0: 1 egg, <= T tosses."""

    def __init__(self, break_flags: list[bool]):
        super().__init__(break_flags)

    def findT(self) -> int:
        for i, b in enumerate(self.bs):
            self.n_toss += 1
            if b:
                return i + 1


class EggDropV1(EggDrop):
    """Egg drop. Version 1: ~ 1*lg(n) eggs and ~ 1*lg(n) tosses."""

    def __init__(self, break_flags: list[bool]):
        super().__init__(break_flags)

    def findT(self) -> int:
        lo, hi = 0, len(self.bs) - 1
        while lo < hi:
            self.n_toss += 1
            mid = lo + (hi - lo) // 2
            if self.bs[mid]:
                self.n_egg += 1
                hi = mid - 1
            else:
                lo = mid + 1
        return lo + 1


class EggDropV2(EggDrop):
    """Egg drop. Version 2: ~ lg(T) eggs end ~ 2*lg(n) tosses."""

    def __init__(self, break_flags: list[bool]):
        super().__init__(break_flags)

    def findT(self) -> int:
        top = len(self.bs) - 1
        i = 1
        while True:
            j = 1
            while True:
                self.n_toss += 1
                if self.bs[(idx := min(i + j - 2, top))]:
                    if j == 1:
                        return idx + 1
                    self.n_egg += 1
                    break
                j *= 2
            i += j // 2


if __name__ == '__main__':
    break_flags = [False] * 250 + [True] * 250

    ED = EggDropV0
    ed = ED(break_flags)
    print(f'{ED.__name__}\t{ed.findT() = }\t{ed.n_egg = }\t{ed.n_toss = }')

    ED = EggDropV1
    ed = ED(break_flags)
    print(f'{ED.__name__}\t{ed.findT() = }\t{ed.n_egg = }\t{ed.n_toss = }')

    ED = EggDropV2
    ed = ED(break_flags)
    print(f'{ED.__name__}\t{ed.findT() = }\t{ed.n_egg = }\t{ed.n_toss = }')
