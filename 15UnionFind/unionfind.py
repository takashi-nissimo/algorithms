from abc import ABCMeta, abstractmethod


class UnionFind(metaclass=ABCMeta):
    """Abstract Class for Union Find"""
    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        pass

    @abstractmethod
    def union(self, p: int, q: int):
        pass


class QuickFindUF(UnionFind):
    """Quick-Find Algorithm for Union Find (Eager Approach)"""

    def __init__(self, N: int):
        self.id = list(range(N))

    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int):
        pid = self.id[p]
        qid = self.id[q]
        for i, _ in enumerate(self.id):
            if self.id[i] == pid:
                self.id[i] = qid


class QuickUnionUF(UnionFind):
    """Quick-Union Algorithm for Union Find (Lazy Approach)"""

    def __init__(self, N: int):
        self.id = list(range(N))

    def root(self, i: int) -> int:
        while (i != self.id[i]):
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j


class WeightedQuickUnionUF(QuickUnionUF):
    """Weighted Quick-Union by size Algorithm for Union Find"""

    def __init__(self, N: int):
        super().__init__(N)
        self._count = N  # number of connected components
        self.sz = [1] * N  # size of each node
        self.largest = list(range(N))  # largest element in each component

    def count(self) -> int:
        """return the number of connected components"""
        return self._count

    def find_largest(self, p: int) -> int:
        """return the largest element in the connected component containing p"""
        return self.largest[self.root(p)]

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        larger = max(self.largest[i], self.largest[j])
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
            self.largest[j] = larger
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            self.largest[i] = larger
        self._count -= 1


class WeightedQuickUnionPathCompressionUF(WeightedQuickUnionUF):
    """Weighted Quick-Union with Path Compression Algorithm for Union Find"""

    def __init__(self, N: int):
        super().__init__(N)

    def root(self, i: int) -> int:
        while (i != self.id[i]):
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i


if __name__ == '__main__':
    from sys import argv
    from pathlib import Path
    with open(Path(argv[1])) as f:
        l = [s.strip() for s in f.readlines()]
    N = int(l.pop(0))
    uf = WeightedQuickUnionPathCompressionUF(N)
    print(f'{N = }, {uf.__class__.__name__}')
    while l:
        p, q = [int(i) for i in l.pop(0).split(' ')]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(
                f'uf.union({p}, {q})',
                f'{uf.count() = }',
                f'{uf.find_largest(0) = }',
            )
