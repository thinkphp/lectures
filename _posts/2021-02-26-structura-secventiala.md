---
layout: post
disqus: y
title: Structura secventiala
---

Structura liniara (secventiala)

Vom defini structura liniara astfel:

Orice operatie de citire/scriere, atribuire, decizionala considerata in ansamblul ei, constituie o structura liniara.

Daca S1 si S2 sunt structuri de orice tip, atunci: 

S1
S2

este o structura liniara.

    instructiune1;
    instructiune2;
    instructiune3;
    --------------
    instructiuneN;
 
Ordinea de executare este: instructiune1, instructiune2, instructiune3....pana la instructiuneN

### Problema 1:

Se citesc doua variabile reale. Sa se interschimbe continutul lor si sa se afiseze.

Solutia in limbajul pseudocod:

    real a, b, aux;
    Citeste a, b
    aux <-- a
    a <--  b
    b <-- aux
    Scrie a, b

Solutia in limbajul de programare c++:

    float a,b,aux;
    cin>>a>>b;
    aux = a;
    a = b;
    b = aux;
    cout<<a<<", "<<b;

### Problema 2:

Se citesc doua valori reale. Sa se afiseze valoarea cea mai mica.

### Problema 3:

Se citesc doua variabile intregi. Sa se interschimbe continutul lor, fara a folosi o variabile auxiliara de manevra.

### Problema 4:

Se citesc doua valori intregi a si b. Se cere sa se afiseze media lor aritmetica.

### Problema 5:

Se citeste un numar natural format din 3 cifre. Se cere sa se afiseze suma cifrelor sale. 

### Problema 6:

Se citesc 3 numere naturale. Se cere sa se afiseze primul numar, suma dintre primul si al doilea, suma primelor trei numere.  
    
     
  




