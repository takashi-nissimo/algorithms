# Union-find
[Lecture Slides](https://d3c33hcgiwev3.cloudfront.net/_b65e7611894ba175de27bd14793f894a_15UnionFind.pdf?Expires=1677715200&Signature=Invyy2BsyaeQiXefu0j1vBGwvMl19JqMOImwCJuiXYMaNnAbgoCPSPJ3ThG4LWKGV08OCrfshgjCml6Oj7W4pgeWSeCszPnrAE19tpNbZPTyG9ykE-kmv1SWFAGek~g~d~8bLM0QQEtDE5~7O2MSCe6qmY1C3A9yPC3bOXL7iGU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

## Scripts
|file|algorithm|
|---|---|
|unionfind.py|UnionFind|
|percolation.py|Percolation|
|successor_with_delete.py|SuccessorWithDelete|

## Performance of Union-find Algorithms
![uf_performance](https://user-images.githubusercontent.com/19323409/219846472-6e943997-08aa-431b-8324-b9dd45d927ba.png)

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