from abc import ABCMeta, abstractmethod


class UF(metaclass=ABCMeta):
    """Abstract Class for Union Find"""
    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        pass

    @abstractmethod
    def union(self, p: int, q: int):
        pass


class QuickFindUF(UF):
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


class QuickUnionUF(UF):
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
        self.sz = [1] * N

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


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
    with open('tinyUF.txt') as f:
        l = [s.strip() for s in f.readlines()]
    N = int(l.pop(0))
    uf = WeightedQuickUnionPathCompressionUF(N)
    while l:
        p, q = [int(i) for i in l.pop(0).split(' ')]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')
