---
layout: post
disqus: y
title: Viete's Formulas
---

In algebra, Vieta's formulas are a set of results that relate the coefficients of a polynomial to its roots. In particular, it states that the elementary symmetric polynomials of its roots can be easily expressed as a ratio between two of the polynomial's coefficients.

C++ Language

```c++
#include <stdio.h>
#include <stdlib.h>
#define VOID 0

double sqrt(double n) {

  double x = n, y = 1.0, e = 0.000001;

  while(x - y > e) {

    x = (x + y) / 2;

    y = n / x;

  }
  return x;
}

void NatureRootsQuadraticEquation(double a, double b, double c) {

    double S = -b/a,
            P = c/a,
            discriminant = b*b - 4*a*c,
            x1, x2;
    x1 = (-b + sqrt(discriminant)) / (2 * a);
    x2 = (-b - sqrt(discriminant)) / (2 * a);
    printf("S=%.2lf P=%.2lf\n",S,P);
    printf("Delta = %.2lf\n\tx1=%lf\n\tx2=%lf\n", discriminant, x1, x2);

    if(discriminant >= 0) {

      if(S >= 0) {

         if(P > 0) {

            printf("%s","x1>0; x2>0");

         } else if(P < 0) {

            printf("%s","x1>0; x2<0; |x1| < |x2|");

         } else {

            printf("%s","x1=0; x2 >0");
         }
      //it means S < 0
      } else {

        if(P > 0) {

           printf("%s","x1<0; x2<0");

        } else if(P < 0) {

           printf("%s","x1>0; x2<0");

        } else {

           printf("%s","x1=0; x2 <0");
        }
      }
    } else {
      printf("Imaginary");
    }
    printf("\n");
}

int main(int argc, char const *argv[]) {
  //declare three variable of double
  double a, b, c;
  a = 1;
  b = 3;
  c = -2;
  //if the number of the arguments is greater than one
  if(argc > 1){
    //convert string to double
    a = atof(argv[1]);
    b = atof(argv[2]);
    c = atof(argv[3]);
  }

  //tests
  if(b < 0 && c < 0) {
       printf("%.3lfx^2 - %.3lfx - %.3lf = 0\n", a, -b, -c);
  } else if(b < 0) {
       printf("%.3lfx^2 - %.3lfx + %.3lf = 0\n", a, -b, c);
  } else if(c < 0) {
       printf("%.3lfx^2 + %.3lfx - %.3lf = 0\n", a, b, -c);
  } else if(a > 0 && b > 0 && c > 0){
       printf("%.3lfx^2 + %.3lfx + %.3lf = 0\n", a, b, c);
  }
  //solve
  printf("%s\n", "Output:");
  NatureRootsQuadraticEquation(a, b, c);

  return VOID;
}
```

```python
def sqrt(n):
    x = n
    y = 1.0
    eps = 0.00001
    while x - y > eps:
        x = (x + y) / 2
        y = n / x
    return x
# Viete's rules = Relatiile lui Viete
# ax^2 + bx + c = 0; a != 0
# x^2 - Sx + P = 0
# S = x1 + x2
# P = x1 * x2
# S = -b/a; P = c/a
# the study of the sign roots of a Quadratic Equation
def Nature_Roots_Quadratic_Equation(a, b, c):
    d = b ** 2 - 4 * a * c
    #a!=0
    S = -b/a
    P = c/a

    print(f"Sum = {S}, Prod = {P}")
    print("Sum = %.2f Prod = %.2f"%(S, P))
    if d < 0:
        return ["imaginary"]
    elif d >= 0:
         x1 = ( -b - sqrt(d) )/ (2*a)
         x2 = ( -b + sqrt(d) ) / (2*a)
         print(f"x1={x1:.2f} x2={x2:.2f}")
         if S > 0:
             if P > 0:
                 return ["x1>0","x2>0"]
             elif P < 0:
                 return ["x1<0","x2>0","|x1|<|x2|"]
                 #x1=-3, x2=7
             else:
                 return ["x1=0","x2>0"]
         # S < 0
         else:
             if P > 0:
                 return ["x1<0","x2<0"]
             elif P < 0:
                 return ["x1<0","x2>0","|x1|>|x2|"]
             else:
                 return ["x1=0","x2<0"]
def main():

    lesson = dict(title = "Viete's Rules", content ="\nNature Roots Quadratic Equation")

    print("Today we'll learn about:\n{title} {content}".format(**lesson))

    A = 1
    B = 5
    C = 2
    print(*Nature_Roots_Quadratic_Equation(A,B,C), sep="\n")

main()

```
 Java Language
```java

import java.util.Scanner;

public class nature {

       public static double sqrt(double n) {
              double x, y, eps = 0.000001;
              x = n;
              y = 1.0;
              while(x - y > eps) {
                x = (x + y) / 2;
                y = n / x;
              }
              return x;
       }

       public static void NatureRootsQuadraticEquation( double a, double b, double c ) {

              double S, P, Delta, x1, x2;

              S = -b/a;
              P = c/a;
              Delta = b*b - 4*a*c;
              System.out.println("\nVerify: ");
              if(Delta < 0) {
                System.out.println("Imaginary");
              } else {
                x1 = (-b-sqrt(Delta))/(2*a);
                x2 = (-b+sqrt(Delta))/(2*a);
                System.out.printf("x1 = %.2f\n",x1);
                System.out.printf("x2 = %.2f\n",x2);
                if( S >= 0 ) {
                    if(P > 0) {
                       System.out.println("x1 > 0 positive, x2 > 0 positive");
                    } else if(P < 0){
                       System.out.println("x1 < 0 negative, x2 > 0 negative, |x1| < |x2|");
                    } else {
                       System.out.println("x1 = 0 ,x2 > 0");
                    }
                //the S < 0 negative
                } else {
                  if(P > 0) {
                     System.out.println("x1 < 0 positive, x2 < 0 negative");
                  } else if(P < 0){
                     System.out.println("x1 < 0 negative, x2 > 0 negative, |x1| > |x2|");
                  } else {
                     System.out.println("x1 = 0 ,x2 < 0");
                  }
                }
              }
       }

       public static void main( String args[] ) {

              double a, b, c;
              Scanner keyboard = new Scanner( System.in );
              if(args.length > 1){
              a = Double.parseDouble(args[0]);
              b = Double.parseDouble(args[1]);
              c = Double.parseDouble(args[2]);
            } else {
              System.out.println("Give A, B, C for Ax^2 + Bx + C = 0: ");
              a = keyboard.nextDouble();
              b = keyboard.nextDouble();
              c = keyboard.nextDouble();
            }
              System.out.printf("The nature of the Roots Quadratic Equation: %.2fx^2 + %.2fx + %.2fc = 0", a, b, c);
              NatureRootsQuadraticEquation(a,b,c);
       }
}

```
