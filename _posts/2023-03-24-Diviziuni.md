---
layout: post
disqus: y
title: Diviziuni
---

# Definitie:

Fie [a,b] un interval inchis si marginit din R. Se numeste diviziune a intervalului [a,b] un sistem de puncte
Δ = (x0,x1,...,xn-1,xn) din [a,b] astfel incat
```
a = x0 < x1 < x2 < ... < xn-1 < xn = b
```

Uneori vom nota diviziunile astfel:

```
Δ = (a = x0 < x1 < x2 < ... < xn = b)
Cea mai mare dintre lungimile intervalelor
[x0,x1],[x1,x2],...,[xn-1,xn] se numeste norma diviziunii Δ
si se noteaza cu ||Δ||
Asadar

||Δ|| = (def) max(1<=i<=n) (xi - xi-1)
```
## Exemple:

Sistemele de puncte

```
Δ1 = (0,1)
Δ2 = (0,1/4,3/4,1)
Δ3 = (0,1/5,1/3,1/2,2/3,4/5,1)

Sunt diviziuni ale intervalului [0,1].
Aceste diviziuni au respectiv normele:
||Δ1|| = 1;
||Δ2|| = 1/2;
||Δ3|| = 1/3;
```

### Observatii:

```
α) Daca [a,b] este un interval, atunci Δ = (a,b) este singura diviziune a lui [a,b] de normala egala cu b - a. Orice alta diviziune a intervalului [a,b] va avea norma strict mai mica decat b - a.
β) Pentru orice numar real r > 0 exista diviziuni Δ ale intervalului [a,b] astfel incat ||Δ|| < r.
Intr-adevar, sa notam cu L lungimea intervalului [a,b]: L = b - a si sa luam un numar natural n astfel incat n > L / r.

Impartind intervalul [a,b] in n parti egale,
obtinem diviziunea Δ = (a, a + L / n,
a + 2 L / n, ..., a + (n-1)L/n,b) care are norma egala cu L / n. Deci ||Δ|| = L / n < r
```
