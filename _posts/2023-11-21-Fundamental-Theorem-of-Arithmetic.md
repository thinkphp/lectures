---
layout: post
disqus: y
title: Fundamental Theorem of Arithmetic
---
The Fundamental Theorem of Arithmetic states that every positive integer $n$ can be written as a product n = p1 p2 p3....pk, pi where the pi are all prime numbers; moreover, this expression for n (called its prime factorization) is unique, up to rearrangement of the factors.

Note that the property of uniqueness is not, in general, true for other sorts of factorizations. For example, most integers have many factorizations into 2 parts: 30 = 2 15 = 3 10 = 5 6. Thus, the Fundamental Theorem of Arithmetic tells us in some sense that "factorizations into prime numbers is deeper than factorization into two parts."

In C++ language:
```c++
#include <stdio.h>

int main(int argc, char const *argv[]) {

  //we declare the variable for our algorithm
  int n, //n input
      i, //start with a variable i
      fm;//multiplicity factor

  printf("%s","Fundamental Theorem of Arithmentic\n");
  printf("%s\n","Source: https://mathworld.wolfram.com/FundamentalTheoremofArithmetic.html");  
  printf("%s","Give a N = ");
  //read an integer
  scanf("%d", &n);

  printf("%d = ", n);
  //start with i equal 2
  i = 2;
  do {

      fm = 0;

      while( (n % i) == 0) {

          fm++;

          n /= i;
      }

      if(n == 1) printf("%d ^ %d", i, fm);
      else
      if( fm!=0 ) printf("%d ^ %d + ", i, fm);


      i++;

  } while(!( n == 1 ));
  printf("\n");

  return 0;
}

```

In Python3 Language
```python
def fta( n ):
    i = 2
    while not (n == 1):
        fm = 0
        while n % i == 0:
            fm += 1
            n //= i
        if fm:
            print(f"{i} ^ {fm}")
        i += 1

def main():
    print("Fundamental Theorem of Arithmentic")
    n = int(input("N = "))
    fta( n )
main()
```

```java
import java.util.Scanner;

public class Main {

       public static void ApplyFTA(int n) {

              int fm, i = 2;

              while(!(n == 1)) {

                     fm = 0;

                     while(n % i == 0) {

                       n /= i;

                       fm += 1;

                     }

                     if( fm != 0 ) System.out.println(i + " ^ " + fm);
                     i += 1;
              }
       }

       public static void main(String args[]) {

              System.out.println("Fundamental Theorem of Arithmetic");

              System.out.print("N = ");

              Scanner keyboard = new Scanner( System.in );

              int n = keyboard.nextInt();

              ApplyFTA( n );
       }
}

```

Reference:
https://artofproblemsolving.com/wiki/index.php/Fundamental_Theorem_of_Arithmetic

Andrei Botorogeanu - Algoritmi si Data Structures.

Problema1: Link1
Problema2: Link2
Problema3: Link3
