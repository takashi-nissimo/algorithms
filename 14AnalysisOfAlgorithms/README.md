# Analysis of Algorithms
[Lecture Slides](https://d3c33hcgiwev3.cloudfront.net/_9e4b178fa46f2b27f7beefbc5b1d2727_14AnalysisOfAlgorithms.pdf?Expires=1677715200&Signature=HMOYkzWe1KDgFaHl-Oh7xnuTKeDOtHZe3Bvzlm3vhCCbCiGTAzCtUUn0xdxQDXQI9uXFtNdw3wv9L19Ukswx-C20hrmxgD3wFhFsPRZ~t6731lzRpdZ~gzimtSxQnH0Zp2SAMOP4RLdFEQX0spbZu5lt6hft-TkwewSgRvMzeD0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

## Scripts
|file|algorithm|
|---|---|
|binarysearch.py|Binary Search|
|threesum.py|3-Sum|
|search_in_bitonic.py|Search in a Bitonic Array|
|eggdrop.py|Egg Drop|

## 3-SUM
Given N distinct integers, how many triples sum to exactly zero?

### Results
```sh
(algorithms) $ python3 threesum.py 400
min(a)=-1995, max(a)=1999, len(a)=400
BruteForceThreeSum      count: 1971     time: 0.8479299545288086
LinearithmicThreeSum    count: 1971     time: 0.1300516128540039
QuadraticThreeSum       count: 1971     time: 0.012657880783081055
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
```
(algorithms) $ python3 eggdrop.py 2048
EggDropV0,      n: 2048,        mean eggs: 1.000,       max eggs: 1,    mean tosses: 1024.500,  max tosses: 2048
EggDropV1,      n: 2048,        mean eggs: 6.500,       max eggs: 12,   mean tosses: 11.000,    max tosses: 12
EggDropV2,      n: 2048,        mean eggs: 6.500,       max eggs: 12,   mean tosses: 39.500,    max tosses: 78
EggDropV3,      n: 2048,        mean eggs: 2.000,       max eggs: 2,    mean tosses: 47.080,    max tosses: 90
EggDropV4,      n: 2048,        mean eggs: 2.000,       max eggs: 2,    mean tosses: 44.646,    max tosses: 65
```