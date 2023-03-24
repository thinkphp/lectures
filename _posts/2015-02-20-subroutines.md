---
layout: post
disqus: y
title: Subroutines
---
# Problems:

1) Se considera un sir de n numere scrise in baza 16. Sa se realizeze un program care determina cel mai mare divizor comun al acestor numere, afisandu-l in baza 10. In cadrul programului, vor fi definite si apelate doua programe:
 - conv function, care primeste un sir de caractere,
 reprezentand un numar in baza 16 si returneaza numarul
 obtinut in urma conversiei in baza 10
 - gcd function, care returneaza cel mai mare divizor comun
 a doua valori transmise prin intermediul a doi parametrii.

```c++
#include <stdio.h>
#include <string.h>

int val(char c) {

    if(c >= '0' && c <= '9') {

       return c - '0';

    } else if(c >= 'A' && c <= 'Z') {

       return c - 'A' + 10;
    }
}
int pw(int a, int b) {

    int p = 1;

    for(int i = 1; i <= b; ++i) {
       p *= a;
    }
    return p;
}

int conv(char s[ 100 ]) {

    int n = strlen( s );

    int num = 0,

        p = 0;

    for(int i = n - 1; i >= 0; --i) {

       num += val(s[i]) * pw(16, p);

       p += 1;
    }
    return num;
}

int gcd( int a, int b ) {

      while( a != b ) {

        if(a > b) {

          a = a - b;

        } else {

          b = b - a;
        }
      }
      return a;
}

int main(int argc, char const *argv[]) {

  char* s[] = {"AA", "BB", "CC", "DD","EE","FF"};

  int n = sizeof(s)/sizeof(s[0]);

  int sol = gcd(conv(s[0]), conv(s[1]));

  for(int i = 2; i < n; ++i) {
          int b = conv(s[i]);
          sol = gcd(sol, b);
  }
  printf("%d", sol);

  return 0;
}

```
```python
def power(a,b):

    p = 1

    for i in range(1,b+1):

        p = p * a

    return p

def val(c):

    if ord(c) >= ord('0') and ord(c) <= ord('9'):

        return ord(c) - ord('0')

    elif ord(c) >= ord('A') and ord(c) <= ord('Z'):

        return ord(c) - ord('A') + 10

def conv( str ):

    base = 16

    n = 0

    p = 0

    for i in range(len(str)-1, -1, -1):

        n = n + val((str[i])) * power(16, p)

        p += 1

    return n

def gcd(a,b):

    while a!=b:

        if a > b:

            a = a - b

        else:

            b = b - a

    return a

def func():

    n = int(input("N="))

    num = input("number1 = ")

    a = conv(num)

    for i in range(2,n+1):
         #convert to decimal
         b = conv(input("numnber%d = "%i))
         # greatest commond divisor
         a = gcd(a, b)

    print(a)

    vec = ["AA","BB","CC"]

    a = conv(vec[0])

    vec.pop(0)

    for i in vec:

        b = conv(i)
        a = gcd(a,b)

    print(a)

func()
```
