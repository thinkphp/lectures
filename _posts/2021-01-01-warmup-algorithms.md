---
layout: post
disqus: n
title: Warmup algorithms
---

We'll begin our study of algorithms in a practical way, looking at four problems and multiple algorithmic solution for each problem. This lets us begin with one of the most important ideas in our field: not only are there many ways to solve a problem, but some solutions - we'll see - can be much more efficient than others.

## First example: Factorial

```python
# iteration
def factorial( n ):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

>>> factorial(5)
>>>120    

# tail recursion
def factorial2( n , a ):

    if n == 1:

       return a

    else:

      return factorial2(n - 1, a * n)     

>>>n = 5
>>>factorial2(n,1)
>>>120
```

```python

# recursion
def factorial3( n ):

    if n == 1:
       return 1
    else:
       return n * factorial3(n - 1)

# Divide et Impera O(n log n) Time Complexity          
def factorial4( first, last ):

    if first == last:
       return first
    else:
        middle = (first + last) >> 1   
        a = factorial4(first, middle)
        b = factorial4(middle + 1, last)
        return a * b

>>> factorial4(1, 5)
>>>120    
```

## Second example: Fibonacci

## Third example: Euclid

## The fourth example: Permutation

## The fifth example: Golbach s Conjecture

## The sixth example: Sequence Collatz
