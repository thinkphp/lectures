---
layout: post
disqus: y
title: Repetition Structure
---


1. Structura repetitiva conditionata anterior:
cat timp ... executa (while)
pentru ... executa (for)

2. Structura repetitiva condtionata posterior:

repeta ... cat timp (do..while)
repeta ... pana cand (do...while(Not(E)))

## Problems:

1. Sa se determine cel mai mare numar care se poate forma
cu ajutorul cifrelor unui numar natural citit de la tastatura.
Input: n = 76134
Output: m = 76431

```python
def solve(n):
    sol = []
    for i in range(9,-1,-1):
        m = n
        count=0
        while m!=0:
            c = m % 10
            if c == i:
                count+=1
            m //= 10
        for j in range(0, count):
            sol.append(i)
    num = 0
    n = len(sol)
    p = 0
    for i in range(n-1, -1, -1):
        num = num + sol[i]*pow(10,p)
        p+=1
    return num

def func():
    n = 56782
    m = solve(n)
    print(m)
func()
```

2. Sa se determine cel mai mic numar care se poate cu cifrele unui numar citit de la tastatura.
Input: n = 76134
Output: m = 13467

```python
def solve(n):
    sol = []
    for i in range(10):
        m = n
        count=0
        while m!=0:
            c = m % 10
            if c == i:
                count+=1
            m //= 10
        for j in range(0, count):
            sol.append(i)
    num = 0
    n = len(sol)
    p = 0
    for i in range(n-1, -1, -1):
        num = num + sol[i]*pow(10,p)
        p+=1
    return num

def func():
    n = 56782
    m = solve(n)
    print(m)
func()
```
