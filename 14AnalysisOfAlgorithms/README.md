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
