---
layout: post
disqus: y
title: Sume Riemann
---

### Definitie:

Consideram urmatoarele obiecte:

* 1) un interval inchis si marginit [a,b];
* 2) o functie [a,b] -> R;
* 3) o diviziune Δ = (x0, x1,...,xn) a intervalului [a,b]
* 4) un sistem de puncte n ξ1, ξ2,...,ξn
astfel incat xi-1 <= ξi <= xi,  (1<=i<=n)

numit sistem de puncte intermediare asociat diviziunii Δ,

* Numarul real:
* Σ(i=1,n)f(ξi)(xi-xi-1)

se numeste suma Riemann asociata functiei f, diviziunii Δ, si punctelor intermediare ξ1,ξ2,...,ξn. Acest numar va fi notat prin
σΔ(f,ξ) sau σΔ(f,ξi).

### Observatie:

Daca functia f este positiva, atunci suma Riemann σΔ(f,ξi) reprezinta suma ariilor dreptunghiurilor de baza xi - xi-1 si de inaltime f(ξi), (1<=i<=n). Deci σΔ(f,ξi) aproximeaza aria multimii din plan, denumita subgraficul lui f,

Γf = {(x,y)apartine lui R^2/ a<=x<=b, 0 <= y <= f(x)},
delimitata de axa Ox, graficul functiei f si dreptele paralele la axa Oy care trec prin punctele de coordonate (a,0), respectiv (b,0)
