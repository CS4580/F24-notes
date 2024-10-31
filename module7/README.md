# Module 7 Notes: Metrics and Model Development


## Metrics

Metrics should be `unbiased`, universal, and concise.
    
1. A way to obtain similar responses
2. A way to measure the performance 
3. A way to measure prediction. 

For our sample analysis we will use `KNN` K-Nearest Neighbor
- `K` is an arbitrary pick
- Need a `base case`
- Compare the neighbors
- Sor the results

Dataset for this analysis: 
```bash
icarus.cs.weber.edu:~hvalle/cs4580/data/movies.csv
```

### KNN-Euclidean Distance

The Euclidean distance is the distance between points in `N-dimensional` space.

Formula
$
d(p, q) = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}
$
where:
- $p = (p_1, p_2, \dots, p_n)$
- $q = (q_1, q_2, \dots, q_n)$

#### Task: 
Find the distance between these points:
- x = (0,0)
- y = (4,4)

Distance = 5.65685...