---
layout: post
disqus: y
title: Integrarea prin parti
---

In acest paragraf si in urmatorul admitem urmatorul rezultat: Orice functie continua f : J -> R admite primitive.

### Teorema:

Formula de integrare prin parti. Daca f, g : J -> R sunt functii derivabile cu derivate continue, atunci functiile
fg, f'g si fg' admit primitive si multimile lor de primitive sunt legate prin relatia:

```
S f(x)g'(x) fx = fg - S g(x) f'(x) fx
```

#### Demonstratie:

Se stie ca orice functie derivabila este continua, deci din ipoteza rezulta ca functiile
f'g si fg' sunt continue, prin urmare si

```
functia (fg)' = f'g + fg' este continua.  (1)
```

Atunci pe baza rezultatului mentionat mai sus, functiile f'g, fg' si (fg)' admit primitive. Aplicand teorema egalitatii, obtinem:
```
S (fg)'(x) dx = S f'(x)g(x) fx + S f(x)g'(x)dx.
Insa observatia:
S (fg)'(x) dx = fg + c (2)
```

din (2) and (3) rezulta:
```
S f(x)g'(x) fx = fg - S g(x) f'(x) fx
```
