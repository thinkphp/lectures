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

15. Sa se calculeze a^n, unde a este un numar real si n este un numar intreg.

```py
# Let's compute a^n
#
# by Adrian
def module(a):
    if a < 0:
        return -(a)
    else:
        return a
def main():

    # let's assume we have a float number
    a = float(input("a = "))
    # let's assume we have an integer number
    n = int(input("n = "))

    r = 1

    if n < 0:
        n = module(n)
        for i in range(1 , n + 1):
            r = r * 1 / a
    else:
        for i in range(1, n+1):
            r = r * a

    print( r )

main()
```

16) Se citeste un numar natural n. Sa se afiseze divizorii sai si numarul lor.


```py
def main():

    N = int(input("N = "))

    count = 0

    for i in range(1, N + 1):

        if N % i == 0:

            print(i)

            count += 1
    print("We have ", count, " divisor!")

main()

```

17) Se citesc N numere naturale nenule. Sa se determine in cate zerori se termina produsul lor fara a efectua inmultirea.

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

18) Sa se calculeze sumele urmatoare, unde x este un numar real si n un numar natural nenul.

E1 = x + x^2 + x^3 + x^4 + ... + x^n

```py
def main():

    x = float(input("x = "))
    n = int(input("n = "))

    p = 1
    s = 0

    for i in range(1,n+1):
        p *= x
        s += p

    print(s)

main()
```
E2 = x + 2 * x^2 + 3 * x^3 + 4 * x^4 + ... + n * x^n

```py
def main():

    x = float(input("x = "))
    n = int(input("n = "))

    p = 1
    s = 0

    for i in range(1,n+1):
        p *= x
        s = s + i * p

    print(s)

main()
```
19) Se citeste un numar natural nenul N. Sa se numere divizorii sai inclusiv 1 si el insusi.

20) Se citeste un numar natural n. Sa se verifice daca el este prim.

```c++
//we need to compile this file as following: gcc main.c -o r -lm
#include <stdio.h>
#include <math.h>

int is_Prime(int n) {

    double result = sqrt((double)n);

    int N = (int)result;

    for(int i = 2; i <= N; ++i) {

        if(n % i == 0) {

          return 0;
        }
    }

    return 1;
}

int isPrime(int n) {

    int i, prime;
    i = 2;
    prime = 1;

    while(i * i <= n && prime) {
      prime = n % i != 0;
      i += 1;
    }
    return prime;
}

int main(int argc, char const *argv[]) {

 for(int n = 2; n <= 20; n++)

  if (is_Prime(n)) {

    printf("%d is prime!\n", n);

  } else {

    printf("%d is not prime!\n", n);
  }

  return 0;

}


```

21) Se citeste un numar natural n. Sa se afiseze divisorii sai proprii si primi.

```py
import math
def main():
    n = 150
    for j in range(2, n):
      if n % j == 0:
        print("Divisor:", j)
        prime = True
        N = int(math.sqrt(j)) + 1
        for i in range(2, N):
            if j % i == 0:
               prime = False
               break
        if prime is True:
            print("prime:", j)

main()
```
