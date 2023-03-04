---
layout: post
disqus: y
title: Spatii Vectoriale
---

The notion of vector space grew up from the discovery by Descartes that points in the Euclidian plane can be represented by ordered pairs of real numbers (and points in 3-dimensional space by ordered triples). We are faced with two completely different descriptions: a point in the plane, or a pair of real numbers. Moreover, operations on vectors look quite different according to which description is used. By example, we add
vectors by the parallelogram law used in mechanics, and we add the real numbers componentwise; but the result is the same.

Fie K un corp comutativ si V o multime nevida. O lege de compozitie externa pe V este o functie f: K x V --> V
Vom nota f(a,x) = ax
Un spatiu vectorial peste corpul K este o multime nevida V astfel incat:

* a) pe V este definita o lege de compozitie interna notata "+" si numita adunare, astfel incat (V,+) este un grup abelian(al carui element neutru se noteaza cu 0).
* b) pe V este definita o lege de compozitie externa f:KxV--> numita inmultire cu scalari(din K), notata (a,x)--> ax,
astfel incat pentru orice a,b din K si orice x,y din V sa avem:

* i) a(x+y) = ax + ay
* ii) (a+b)x = ax + bx
* iii) a(bx) = (ab)x
* iv) 1x = x
Elementele lui V se numesc vectori, iar elementele lui K, scalari.

# Exemple:

1. K = R si V = R^2 = R x R. Adunarea in V
se defineste prin (x,y) + (x',y') = (x + x',y + y'), iar inmultirea cu scalari prin
a(x+y) = ax + ay

2. K = R si V = R^3 = R * R * R

3. K = R si V = M2(R). In raport cu operatia de adunare a matricelor si cea de inmultire a matricelor cu numere, V este un spatiu vectorial peste R. Analog pentru M3(R).

4. Fie sistemul liniar omogen:

* a11x + a12y + a13z = 0
* a21x + a22y + a23z = 0
* a31x + a32y + a33z = 0

aih apartine lui R si S multimea solutiilor sale care este o submultime nevida a lui R^3. Cu operatiile definite in R^3, S
este un spatiu vectorial peste R.
