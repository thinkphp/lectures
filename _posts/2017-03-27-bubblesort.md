---
layout: post
disqus: y
title: Bubble Sort
---

Bubblesort
----------


We come now to the family of sorting algorithms: exchange or transposition methods which systematically interchange pairs of elements that are out of order until no more such pairs exist.

The bubble sort. We compare K(1) with K(2), interchange R(1) with R(2) if the keys are out of order; then we do the same to R(2) and R(3), R(3) and R(4) etc. During this sequence of operations, records with large keys will move up. Repetitions of the process wil get the apropriate records into positions R(N), R(N-1), R(N-2) etc. so that all records will ultimately be sorted.

The method is called bubble sorting because large elements bubble up to their proper position. After each pass through the file, it is not hard to see that all records above and including the last one to be exchanged must be in their final position, so they need not be examined on subsequence passes.

``` ruby

Algorithm B (Bubble Sort). Records R(1),...,R(N) are rearranged
in place; after sorting is complete their keys will be in
order, K(1)<=K(2)<= ...<=K(N).

1. Set BOUND <-- N (BOUND is the highest index for which
   the record is known to be in its final position).

2. Set t <-- 0, Perform step 3 for j=1,2,...,BOUND - 1, and then go to step 4

3. If K(j) > K(j+1) , interchange R(j) <--> R(j+1) and set t <-- j.

4. If t = 0 , the algorithm terminates, otherwise set BOUND <-- t 
and return to step 2.

```