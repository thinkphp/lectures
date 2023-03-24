---
layout: post
disqus: y
title: Sequentially Structure
---

Orice operatie de citire/scriere, atribuire, decizionala considerata in ansamblul ei, constituie o structura liniara.

```
statement1
statement2
..........
statement3
```




Ordinea de executare este: instructiune1, instructiune2, instructiune3....pana la instructiuneN

# Problems

1) Se citesc doua variabile reale. Sa se interschimbe continutul lor si sa se afiseze.

```
    real a, b, aux;
    Citeste a, b
    aux <-- a
    a <--  b
    b <-- aux
    Scrie a, b
```    

```c++
    float a,b,aux;
    cin>>a>>b;
    aux = a;
    a = b;
    b = aux;
    cout<<a<<", "<<b;
```    

2) Realizati un algoritm pentru calculul expresiilor urmatoare:
```
A = 2 + x - y
B = x * A + 2 + y
C = A - 2 * B + x
```
3) Se citesc doua valori reale. Sa se afiseze valoarea cea mai mica (sau cea mai mare).
```python
```
```c++
```


4) Se citesc doua valori reale. Sa se afiseze valoarea cea mai mica (sau cea mai mare) fara a utiliza operatorul de comparatie.Let’s compute the Max of Two without IF Statement Control Flow.(<,>)
```python
```
```c++
```


5) Realizati un algoritm pentru determinarea perimetrului si ariei unui triunghi caruia i se cunosc lungimile laturilor.

```python
```
```c++
```

6) Se citesc doua variabile intregi. Sa se interschimbe continutul lor, fara a folosi o variabile auxiliara de manevra.
```python
```
```c++
```


7) Se citesc doua valori intregi a si b. Se cere sa se afiseze media lor aritmetica.
```python
```
```c++
```


8) Se citeste un numar natural format din 3 cifre. Se cere sa se afiseze suma cifrelor sale.
```python
```
```c++
```


9) Se citesc 3 numere naturale. Se cere sa se afiseze primul numar, suma dintre primul si al doilea, suma primelor trei numere.  
```python
```
```c++
```

10) Realizati un algoritm pentru determinarea perimetrului si ariei unui patrat caruia i se cunoaste lungimea laturii sale.
```python
```
```c++
```
