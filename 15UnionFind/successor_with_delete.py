"""Successor with delete. 
Given a set of N integers S = {0, 1, ..., N-1}
and a sequence of requests of the following form:
 - Remove x from S
 - Find the successor of x: the smallest y in S such that y >= x.
design a data type so that all operations (except construction) should take
logarithmic time or better.
"""

from unionfind import WeightedQuickUnionUF as UF


class SuccessorWithDelete():

    def __init__(self, n: int):
        self.n = n
        self.data = [True] * n
        self.uf = UF(n)

    def remove(self, x: int):
        self.data[x] = False
        if x > 0 and not self.data[x - 1]:
            self.uf.union(x, x - 1)
        if x < self.n - 1 and not self.data[x + 1]:
            self.uf.union(x, x + 1)

    def successor(self, x: int) -> int:
        if self.data[x]:
            return x
        y: int = self.uf.find_largest(x) + 1
        if y < self.n:
            return y


if __name__ == '__main__':
    from sys import argv
    from random import sample

    n = int(argv[1])
    swd = SuccessorWithDelete(n)
    for i in sample(range(n), k=n):
        swd.remove(i)
        print(f'remove({i}) ->',
              f'successors: {[swd.successor(j) for j in range(n)]}')
