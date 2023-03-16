---
layout: post
disqus: y
title: Retele de transporturi
---

# Definitie:

Fie G = (V, E) un graf orientat. Se numeste retea de transport ansamblul R = (G, st, fin, c) unde 

* G este un graf orientat 
* st apartine lui V si d+(st) > 0, d-(st) = 0
* fin apartine lui V si d-(st) > 0, d+(st) = 0, fin != st
* c : V x V -> N, Daca [i, j] nu apartine lui E, atunci C(i,j) = 0

## Exemple:

Mai jos puteti observa o retea de transport in care st este nodul 1, fin este nodul 7, iar valorile diferite de 0 ale functiei c sunt trecute pe arcuri:

![image]( {{site.baseurl}}{{ site.imageurl }}network-flow.png)

Semnificatie:

De la st la fin trebuie transportat ceva anume. Functia c are semnificatia de capacitate de transport intre oricare doua noduri.

O retea de transport se citeste dintr-un fisier text  cu datele organizate ca mai jos:

Linia 1   n numarul de noduri
Linia 2 - st and fin 
Urmatoarele linii sunt de forma i j c si au semnificatia ca de la nodul i de nodul j exista capacitatea de transport c.

* 7
* 1 7
* 1 2 1
* 2 3 8
* 3 7 1
* 1 4 5
* 4 3 3
* 2 5 4
* 5 6 5
* 7 7 8

## Bibliografie:

1. https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/7c2927794e61bd70c14c07728fa54375_MIT6_046JS12_lec13.pdf
