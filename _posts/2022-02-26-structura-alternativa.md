---
layout: post
disqus: y
title: Structura alternativa
---
Daca S1 si S2 sunt structuri si E este o conditie. Atunci:
```
Daca E atunci

     S1

  altfel

     S2
```

este o structura alternativa.

Modul de executare este urmatorul:

- se evalueaza conditia;
- daca aceasta este indeplinita se executa S1, altfel se executa S2

Forma simplificata a structurii alternative este:

Daca E atunci
     instructiune;

Daca la evaluare E returneaza True se executa instructiune, altfel se trece mai departe.

## Problems:

1) Sa se scrie un algoritm care citeste un numar natural (comanda). Daca acesta este 0 se vor citi doua numere intregi a si b
si se va afisa suma lor, contrar se vor citi doua numere reale x si y si se va afisa suma lor.

In pseudocode language:
```
intreg comanda, a, b, s1
real x, y, s2
Citeste comanda
Daca comanda = 0 atunci

     Citeste a, b
     s1 <-- a + b
     Scrie s1

   altfel
     Citeste x, y
     s2 <-- x + y
     Scrie s2
```

In C++ programming language

```
  int comanda, a, b, s1;
  float x, y, s2;
  cin>>comanda;
  if(comanda == 0) {
        cin>>a>>b;
        s1 = a + b;
        cout<<s1;
  } else {
        cin>>x>>y;
        s1 = x + y;
        cout<<s2;
  }
```
2) Se citesc doua numere reale a si b. Sa se rezolve ecuatia de gradul 1: ax + b = 0
```python
```


3) Se citesc trei numere reale a, b si c. Sa se rezolve ecuatia de gradul 2: ax^2 + bx + c = 0
```python
```


4) Se considera doua puncte in plan, exprimate prin perechi de coordonate (x,y). Ele reprezinta centrele a doua cercuri de raza R1, respectiv R2. Sa se verifice daca cele doua cercuri sunt tangente interne, tangente externe, secante sau exterioare.

```python
```
