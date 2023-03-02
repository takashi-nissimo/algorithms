# Analysis of Algorithms
[Lecture Slides](https://www.coursera.org/learn/algorithms-part1/supplement/mpK20/lecture-slides)

## Scripts
|file|algorithm|
|---|---|
|binarysearch.py|Binary Search|
|threesum.py|3-Sum|
|search_in_bitonic.py|Search in a Bitonic Array|
|eggdrop.py|Egg Drop|

## Binary search

### Results
```shell-session
(algorithms) $ python3 binarysearch.py 
a = [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
binary_search(a, -20) = 0
binary_search(a, 18) = 19
binary_search(a, 10) = 15
binary_search(a, 11) = None
```

## 3-SUM
Given N distinct integers, how many triples sum to exactly zero?

### Results
```shell-session
(algorithms) $ python3 threesum.py 400
min(a)=-1995, max(a)=1999, len(a)=400
BruteForceThreeSum      count: 1971     time: 0.8479299545288086
LinearithmicThreeSum    count: 1971     time: 0.1300516128540039
QuadraticThreeSum       count: 1971     time: 0.012657880783081055
```

## Search in a bitonic array
An array is bitonic if it is comprised of an increasing sequence of integers
followed immediately by a decreasing sequence of integers.
Write a program that, given a bitonic array of n distinct integer values,
determines whether a given integer is in the array.
- Standard version: Use ~ 3 lg n compares in the worst case.
- Signing bonus: Use ~ 2 lg n compares in the worst case
(and prove that no algorithm can guarantee to perform fewer than ~ 2 lg n compares in the worst case).

### Results
```shell-session
(algorithms) $ python3 search_in_bitonic.py 20 1000
n = 20, trials = 1000, mean_worst_time = 3.0491352081298827e-06
(algorithms) $ python3 search_in_bitonic.py 40 1000
n = 40, trials = 1000, mean_worst_time = 3.67283821105957e-06
(algorithms) $ python3 search_in_bitonic.py 60 1000
n = 60, trials = 1000, mean_worst_time = 5.14531135559082e-06
(algorithms) $ python3 search_in_bitonic.py 80 1000
n = 80, trials = 1000, mean_worst_time = 4.8894882202148435e-06
(algorithms) $ python3 search_in_bitonic.py 100 1000
n = 100, trials = 1000, mean_worst_time = 6.241321563720703e-06
```

## Egg Drop
Suppose that you have an n-story building (with floors 1 through n)
and plenty of eggs. An egg breaks if it is dropped from floor T or higher
and does not break otherwise. Your goal is to devise a strategy to determine
the value of T given the following limitations on the number of eggs and tosses:
- Version 0: 1 egg, <= T tosses.
- Version 1: ~ 1\*lg(n) eggs and ~ 1\*lg(n) tosses.
- Version 2: ~ lg(T) eggs end ~ 2\*lg(n) tosses.
- Version 3: 2 eggs and ~ 2*sqrt(n) tosses.
- Version 4: 2 eggs and <= c*sqrt(T) tosses for some fixed constant c.

### Results
```shell-session
(algorithms) $ python3 eggdrop.py 2048
EggDropV0,      n: 2048,        mean eggs: 1.000,       max eggs: 1,    mean tosses: 1024.500,  max tosses: 2048
EggDropV1,      n: 2048,        mean eggs: 6.500,       max eggs: 12,   mean tosses: 11.000,    max tosses: 12
EggDropV2,      n: 2048,        mean eggs: 6.500,       max eggs: 12,   mean tosses: 39.500,    max tosses: 78
EggDropV3,      n: 2048,        mean eggs: 2.000,       max eggs: 2,    mean tosses: 47.080,    max tosses: 90
EggDropV4,      n: 2048,        mean eggs: 2.000,       max eggs: 2,    mean tosses: 44.646,    max tosses: 65
```
