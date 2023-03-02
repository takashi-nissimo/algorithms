# Union-find
[Lecture Slides](https://www.coursera.org/learn/algorithms-part1/supplement/bcelg/lecture-slides)

## Scripts
|file|algorithm|
|---|---|
|unionfind.py|UnionFind|
|percolation.py|Percolation|
|successor_with_delete.py|SuccessorWithDelete|

## Union-find

### Performance of Union-find Algorithms
![uf_performance](https://user-images.githubusercontent.com/19323409/219846472-6e943997-08aa-431b-8324-b9dd45d927ba.png)

### Results
```sh
(algorithms) $ python3 unionfind.py tinyUF.txt 
N = 10, WeightedQuickUnionPathCompressionUF
uf.union(4, 3) uf.count() = 9 uf.find_largest(0) = 0
uf.union(3, 8) uf.count() = 8 uf.find_largest(0) = 0
uf.union(6, 5) uf.count() = 7 uf.find_largest(0) = 0
uf.union(9, 4) uf.count() = 6 uf.find_largest(0) = 0
uf.union(2, 1) uf.count() = 5 uf.find_largest(0) = 0
uf.union(5, 0) uf.count() = 4 uf.find_largest(0) = 6
uf.union(7, 2) uf.count() = 3 uf.find_largest(0) = 6
uf.union(6, 1) uf.count() = 2 uf.find_largest(0) = 7
```

## Percolation
[specification](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php)

<img src=https://coursera.cs.princeton.edu/algs4/assignments/percolation/percolates-yes.png width=400>

### Results
```sh
(algorithms) $ python3 percolation.py 200 100
mean                    = 0.5924785
stddev                  = 0.009659263766724227
95% confidence interval = [0.5905852843017221, 0.594371715698278]
total_running_time = 11.621068239212036 [s]
total_memory_usage = 2093104 [bytes]
(algorithms) $ python3 percolation.py 2 10000
mean                    = 0.664775
stddev                  = 0.1185088765045937
95% confidence interval = [0.66245222602051, 0.66709777397949]
total_running_time = 0.20238757133483887 [s]
total_memory_usage = 656 [bytes]
```

## Successor with delete
Given a set of N integers S = {0, 1, ..., N-1}
and a sequence of requests of the following form:
 - Remove x from S
 - Find the successor of x: the smallest y in S such that y >= x.
design a data type so that all operations (except construction) should take
logarithmic time or better.

### Results
```sh
(algorithms) $ python3 successor_with_delete.py 8
remove(0) -> successors: [1, 1, 2, 3, 4, 5, 6, 7]
remove(6) -> successors: [1, 1, 2, 3, 4, 5, 7, 7]
remove(3) -> successors: [1, 1, 2, 4, 4, 5, 7, 7]
remove(4) -> successors: [1, 1, 2, 5, 5, 5, 7, 7]
remove(7) -> successors: [1, 1, 2, 5, 5, 5, None, None]
remove(1) -> successors: [2, 2, 2, 5, 5, 5, None, None]
remove(5) -> successors: [2, 2, 2, None, None, None, None, None]
remove(2) -> successors: [None, None, None, None, None, None, None, None]
```
