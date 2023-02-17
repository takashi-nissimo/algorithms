from random import sample
from statistics import mean, stdev
from math import sqrt
from functools import cache

from unionfind import WeightedQuickUnionUF as UF


class Percolation():

    def __init__(self, n: int):
        """creates n-by-n grid, with all sites initially blocked"""
        self.n = n
        self.grid = [[False] * n for _ in range(n)]
        self.uf = UF(n ** 2 + 2)  # n-by-n grid sites + 2 virtual sites

    def open(self, row: int, col: int):
        """opens the site (row, col) if it is not open already"""
        if self.isOpen(row, col):
            return
        self.grid[row][col] = True
        site = row * self.n + col

        # look top
        if row == 0:
            self.uf.union(site, -1)  # union with virtual top site
        elif self.isOpen(row - 1, col):
            self.uf.union(site, site - self.n)

        # look bottom
        if row in (self.n - 1, -1):
            self.uf.union(site, -2)  # union with virtual bottom site
        elif self.isOpen(row + 1, col):
            self.uf.union(site, site + self.n)

        # look left
        if col > 0 and self.isOpen(row, col - 1):
            self.uf.union(site, site - 1)

        # look right
        if col < self.n - 1 and self.isOpen(row, col + 1):
            self.uf.union(site, site + 1)

    def isOpen(self, row: int, col: int) -> bool:
        """is the site (row, col) open?"""
        return self.grid[row][col]

    def isFull(self, row: int, col: int) -> bool:
        """is the site (row, col) full?"""
        return self.uf.connected(-1, row * self.n + col)

    def numberOfOpenSites(self) -> int:
        """returns the number of open sites"""
        return sum(sum(row) for row in self.grid)

    def percolates(self) -> bool:
        """does the system percolate?"""
        return self.uf.connected(-1, -2)


class PercolationStats():

    def __init__(self, n: int, trials: int):
        """perform independent trials on an n-by-n grid"""
        self.trials = trials
        self.z = 1.96

        self.thrs = []
        for _ in range(trials):
            percolation = Percolation(n)
            for site in sample(range(n ** 2), n ** 2):
                percolation.open(*divmod(site, n))
                if percolation.percolates():
                    self.thrs.append(percolation.numberOfOpenSites() / n ** 2)
                    break

    @cache
    def mean(self) -> float:
        """sample mean of percolation threshold"""
        return mean(self.thrs)

    @cache
    def stddev(self) -> float:
        """sample standard deviation of percolation threshold"""
        return stdev(self.thrs)

    @cache
    def confidenceLo(self) -> float:
        """low endpoint of 95% confidence interval"""
        return self.mean() - self.z * self.stddev() / sqrt(self.trials)

    @cache
    def confidenceHi(self) -> int:
        """high endpoint of 95% confidence interval"""
        return self.mean() + self.z * self.stddev() / sqrt(self.trials)

    def print(self):
        """print percolation stats"""
        print(f'mean\t\t\t= {self.mean()}')
        print(f'stddev\t\t\t= {self.stddev()}')
        print('95% confidence interval\t= [{}, {}]'.format(
            self.confidenceLo(), self.confidenceHi()))


if __name__ == '__main__':
    from sys import argv
    from time import time

    n = int(argv[1])
    traials = int(argv[2])

    start_time = time()
    stats = PercolationStats(n, traials)
    total_running_time = time() - start_time

    p = Percolation(n)
    total_memory_usage = p.grid.__sizeof__() + p.uf.__sizeof__()

    stats.print()
    print(f'{total_running_time = } [s]')
    print(f'{total_memory_usage = } [bytes]')
