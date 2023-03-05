---
layout: post
disqus: y
title: Repetition Structure
---


* Structura repetitiva conditionata anterior:
cat timp ... executa (while)
pentru ... executa (for)

* Structura repetitiva condtionata posterior:

repeta ... cat timp (do..while)
repeta ... pana cand (do...while(Not(E)))

## Problems:

1) Se citeste un numar natural n, diferit de 0. Sa se afiseze suma cifrelor sale.
```python

```

```c
```


2) Se citeste un numar natural n. Sa se afiseze numarul obtinut prin inversarea numarului citit.
```python
```
```c++
```

3) Se citeste un numar natural de cel mult 8 cifre. Sa se formeze un alt numar din cifrele situate pe pozitii impare (de la stanga la dreapta).

```python
def func():
    n = 123567
    x = 0
    while n!=0:
        x = x * 10 + n % 10
        n //= 10

    while x!=0:
        n = n * 10 +  x % 10
        x //= 100
    print(n)
func()
```

4) Se citesc numerele naturale n1 si n2. Sa se calculeze produsul lor, fara a utiliza operatorul de inmultire.
```python
```
```c++
```

5) Se citesc doua numere naturale n1 si n2. Se cere sa se calculese catul si restul impartirii intregi a lui n1 la n2 fara a utiliza operatorul de impartire.
```python
```
```c++
```

6) Se citeste un numar natural n. Se cere sa se calculese suma primelor n numere naturale.
input: n = 10
output: s = 1 + 2 + 3 + 4 + ... + 10 = 5050
```python
```
```c++
```

7) Sa se calculeze suma:
0,1 + 0,2 + 0,3 + ... + 0.9
```python
```
```c++
```

8) Se citeste un numar natural n. Se cere sa se calculeze suma:
1 + 1 * 2 + 1 * 2 * 3 + 1 * 2 * 3 * 4 + ...+ 1 * 2 * 3 * 4 * ...n
```python
```
```c++
```

9) Sa se determine cel mai mare numar care se poate forma
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

10) Sa se determine cel mai mic numar care se poate cu cifrele unui numar citit de la tastatura.
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
