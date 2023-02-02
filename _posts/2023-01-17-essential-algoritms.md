---
layout: post
disqus: n
title: Essentials Algoritms
---

### A Set of Problems which processes simple data:

1. Se citesc doua numere reale a si b. First Degree Equation: ax + b = 0

2. Se citesc trei numere reale a, b, and c. Sa se rezolve ecuatia de gradul al doilea: ax^2 + bx + c = 0

3. Se citesc coeficientii reali a, b, c al unei ecuatii de gradul al doilea ax^2 + bx + c = 0 (a!=0). Fara a rezolva ecuatia, precizati
semnul radacinilor si natura acestora.
Example: a = 2, b = 10, and c = 3 -> ecuatia are radacinile x1, x2 < 0 reale.

4. Sa se determine suma a doua intervale de date in ore, minute si secunde. (ora < 24, minute < 60, secunde < 60)

5. ```Fie expresia E = |a - b|. ```
   Evaluati expresia a si b, numere reale.

6. Fie expresia E = a/Radical(b). Sa se evalueze aceasta expresie
pentru a si b numere reale.

7. Sa se calculeze valoarea expresiei
```
     a + b, daca c < 1
E =      
     a - b, daca c >= 1
```     
      unde a, b, c sunt numere reale.

8. Fie expresia E = (a + b) / (c - d). Sa se calculeze valoarea lui E, unde a, b, c, d sunt numere reale.

9. Let's compute Max of Three.

10. Let's compute the Max of Two without IF Statement Control Flow.

11. Se citesc trei numere intregi a, b, c. Sa se calculeze maximul lor.
    ```
    Read a, b, c
    max <-- a
    if b > max then
       max <---b
    if c > max then
       max <-- c
    Write max   
    ```      
12. Se citeste latura l (numar natural nenul) a unui patrat.
Sa se calculeze diagonala si aria sa.
13. Se citesc a, b, c numere naturale, reprezentand lungimile
laturilor unui triunghi. Calculati aria sa.
```
Read a, b, c
p <-- (a + b + c) / 2
Area <-- Radical(p * (p - a) (p - b) (p - c))
Write Area
```
14. Sa se verifice ca punctele din plan A (ax, ay), B (bx, by) and C(xc,yc) sunt coliniare.

15. Se citesc N numere naturale nenule. Sa se determine in cate
zerori se termina produsul lor fara a efectua inmultirea.

```py
def zero():

    # How many numbers
    N = int(input("N = "))

    x = 0
    y = 0

    for i in range(N):

        two = 0
        five = 0

        num = int(input("num = "))

        while num % 2 == 0:
              two += 1
              num /= 2

        while num % 5 == 0:
              five += 1
              num /= 5

        x += two
        y += five

    if x < y:
       print(x, " Zeros")
    else:
       print(y, " Zeros")
zero()
```


```c++
#include <stdio.h>

//main function
int main(int argc, char const *argv[]) {

  //define the input variables
  int N,
      num,
      x,
      y,

  //define the output variables
      two,
      five;

  //print the number of the array
  printf("N = ");
  //read it
  scanf("%d", &N);

  x = 0;
  y = 0;

  //loop through the array of the integers
  for(int i = 0 ; i < N; ++i) {

       printf("num = ");
       scanf("%d", &num);

        two = 0;
        five = 0;

       while(num % 2 == 0) {
            two += 1;
            num /= 2;
       }

       while(num % 5 == 0) {
            five += 1;
            num /= 5;
       }

       x += two;
       y += five;
  }

  if(x < y)
    printf("%d zeros",x);
  else
    printf("%d zeros",x);

  return 0;
}

```
