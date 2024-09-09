---
layout: post
disqus: y
title: Operatiile pe care le efectueaza un algoritm
---

### Operatiile pe care le efectueaza un algoritm

In linii mari, operatiile pe care le efectueaza un algoritm se impart in trei mari categorii:

- Operatii de intrare/iesire
- operatii de atribuire
- operatii de decizie

#### 1. Operatii de intrare / iesire 

Am aratat ca orice algoritm lucreaza cu date de intrare si de iesire. Acestea pot fi citite si scrise.

Prin operatia de intrare (de citire) se intelege preluarea unei date de la un dispozitiv de intrare catre memoria interna a calculatorului, catre memoria RAM, adica catre
memoria rezervata pentru aceasta, adica in variabila. Dispozitivele de intrare pot fi tastatura, cel mai des utilizata), unitate de disk, etc.

In limbajul pseudocod vom folosi pentru citire operatia Citeste.

Prin operatia de iesire (scriere) se intelege preluarea unei date din memoriea interna , adica dintr-o variabila, si transeferul ei catre un dispozitiv de iesire. 
Dispozitivele de iesire pot fi: monitorul, imprimanta, etc.

Pentru scriere vom folosi operatia Scrie.

Deocamdata vom presupune ca dispozitivul de intrare este tastatura, iar cel de iesire este monitorul.

Sa analizam algoritmul de mai jos - scris in limbajul pseudocod - care citeste un numar intreg si-l tipareste pe ecran:

intreg a
citeste a
scrie a

Mai intai am declarat o variabila a, de tip intreg - adica are posibilitatea de a retine numere intregi. Urmeaza sa se efectueze operatia de citire
a variabilei a. Aceasta inseamna ca se asteapta introducerea de la tastatura a datei intregi. In cazul in care introducem numarul 8, variabila a va retine 8, daca introducem
10, variabila a va retine 10.
  
  | 8 |
  
  a
  
  La scriere apare pe monitor numarul 8 - continutul variabilei a.
  
  Observatii:
  
  Dupa scriere, continutul variabile ramane neschimbat.
  
  Fie secventa de la jos. Introducem de la tastatura 17. Pe monitor va apare de doua ori numarul 17.
  
  intreg a
  citeste a
  scrie a
  scrie a
  
  La o noua citire, continutul vechi al variabilei se pierde.
  
  intreg a
  citeste a
  citeste a
  Scrie a
  
  Se pot citi mai multe variabile cu o singura opeatie Citeste si se pot tipari valorile retinute de mai multe variabile cu o singura operatie Scrie.
  
  real a,b,c,d
  citeste a,b,c,d
  scrie a,b,c,d
  
#### 2. Atribuiri

  Prin operatia de atribuire se retine o anumita data intr-o variabila. Ea are mai multe forme, pe care le vom prezenta pe rand.

  Forma 1:

  v <-- data

  Semnificatia este urmatoarea:
  
  - v este numele unei variabile de un tip oarecare.
  <-- notatia pentru operatia de atribuire
  data - o valoare pentru un tip oarecare.

  Cu o singura exceptie, tipul variabilei trebuie sa coincida cu tipul valorii atribuite.

  Exemple:

  intreg a;
  a <-- 10 

  variabila a va retine 10

  real b
  b <-- 7.23

  variabila b va retine 7.23

  sir c
  c <-- 'this is a String'

  Variabila c va retine valoarea de tip sir 'this is a string'

  Exceptia este urmatoarea: unei variabile de tip real i se poate atribui o valoare de tip intreg.

  real d
  d <-- 7

  Forma 2:

  v1 <-- v2

  unde v1 si v2 sunt nume de variabile. Cu o exceptie, tipul celor doua variabile trebuie sa coincida. Efectul este ca variabila
  v1 va retine continutul variabilei v2. Dupa aplicarea acestei operatii, continutul variabilei v2 ramane nemodificat, in timp ce 
  continutul variabilei v1 se pierde.

  Exemplul 1:
  Fie a o variabila de tip intreg care retine valoarea 2. Variabila b este de acelasi tip cu variabila a si retine numarul 3. 
  consideram atribuirea a <-- b. Continutul celor doua variabile este:
  a: 2
  b: 3

  Dupa atribuire continutul celor doua variabile va fi:

  a: 3
  b: 3

  Forma 3:

  
