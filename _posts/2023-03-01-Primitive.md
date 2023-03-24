---
layout: post
disqus: y
title: Primitive
---

Fiind data o functie f : J -> R (J un interval inclus in R), se pun urmatoarele
probleme:
* (A) Exista (si in ce conditii) o functie F: J ->R a carei derivata sa fie functia data f?
* (B) Cum se poate determina o asemenea functie F, pornind de la f?
* In acest curs vom studia cateva metode de obtinere a functiilor F care verifica relatia
F' = f.
Raspunsul la problema (A) este afirmativ pentru o clasa destul de larga de functii, in particular pentru functiile continue.

# Definitie:

Fie J un interval inclus in R si f:J->R. Spunem ca f admite primitiva pe J daca exista o functie F:J->R astfel incat:
*1) F este derivabila pe J
*2) F'(x) = f(x), oricare ar fi x din J.

Funtia F se numeste primitiva a functie f.

Daca intervalul J este inchis la stanga si a este o extremitatea sa stanga, atunci prin derivata lui F in punctul a se subintelege derivata la dreapta a lui F in a. O conventie analoga se face cand J este inchis la dreapta.

# Exemple:

1) Fie n apartine lui N si f:R->R functie definita prin relatia:
f(x) = x^n, oricare ar fi x din R.
Atunci pentru orice numar real fixat c,

* functia Fc(x) = 1 / (n + 1) x ^ n + 1 + c, oricare ar fi x din R, este o primitiva a lui f.

2) Functia F(x) = (sin x)^2, oricare ar fi x din R este o primitiva a functiei f(x) = 2sinxcosx

3) Daca a > 0, a != 1, atunci functia
F(x) = a^x / ln a, oricare ar fi x din R.
este o primitiva a functiei f(x) = a^x, oricare ar fi x din R.
