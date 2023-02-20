"""
Successor with delete. 
Given a set of N integers S={0,1,...,N?1} and a sequence of requests of the following form:
 - Remove x from S
 - Find the successor of x: the smallest y in S such that y>=x.
design a data type so that all operations (except construction) should take logarithmic time or better.
"""

from unionfind import WeightedQuickUnionUF as UF


class SuccessorWithDelete():

    def __init__(self, N: int):
        self.N = N
        self.data = [True] * N
        self.uf = UF(N)

    def remove(self, x: int):
        self.data[x] = False
        if x > 0 and not self.data[x - 1]:
            self.uf.union(x, x - 1)
        if x < self.N - 1 and not self.data[x + 1]:
            self.uf.union(x, x + 1)

    def successor(self, x: int) -> int:
        if self.data[x]:
            return x
        y: int = self.uf.find_largest(x) + 1
        if y < self.N:
            return y
        else:
            print(f'Error, no successor of {x=} can be found')
            return -1


if __name__ == '__main__':
    swd = SuccessorWithDelete(N=10)
    swd.remove(2)
    print(swd.successor(2) == 3)
    swd.remove(3)
    print(swd.successor(2) == 4)
    print(swd.successor(8) == 8)
    swd.remove(8)
    print(swd.successor(8) == 9)
    swd.remove(9)
    print(swd.successor(8) == -1)
    swd.remove(5)
    swd.remove(4)
    print(swd.successor(3) == 6)
