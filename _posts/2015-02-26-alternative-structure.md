---
layout: post
disqus: y
title: Alternative Structure
---
Daca S1 si S2 sunt structuri si E este o conditie, atunci:
```
Daca E atunci
     S1
altfel
     S2
```

este o structura alternativa.

Modul de executare este urmatorul:

- se evalueaza conditia;
- daca aceasta este indeplinita se executa S1, altfel se executa S2


## Problems:

1) Se citesc trei numere intregi a, b, c. Sa se afiseze in ordine crescatoare:

```python
def main():
  a, b, c = 1, -2, -3
  if a < b:
    if c < a:
      print(c, a, b)
    elif c < b:
      print(a, c, b)
    else:
      print(a, b, c)
  else:
    if c < b:
      print(c, b, a)
    elif c < a:
      print(b, c, a)
    else:
      print(b, a, c)
main()
```
```c++
```

2) Se considera o fractie a carei numitor este un numar prim. Sa se verifice daca este ireductibila, reductibila, subunitara sau supraunitara.
```c++
```
```python

def func():

      a = int(input("a="))
      b = int(input("b="))

      if a % b == 0:
          print("Reducible.")
      elif a % b != 0:
          print("Ireducible.")
      if a > b:
          print("Superunitary.")
      else:
          print("Subunit.")

func()          

```
3) Considerand cunoscute trei valori reale, verificati daca ele pot reprezenta lungimile laturilor unui triunghi, iar in caz afirmativ determinati tipul acestuia: isoscel, echilateral, dreptunghic sau oarecare.
```c++
```
```python
```


4) Sa se scrie un algoritm care citeste un numar natural (comanda). Daca acesta este 0 se vor citi doua numere intregi a si b
si se va afisa suma lor, contrar se vor citi doua numere reale x si y si se va afisa suma lor.

In pseudocode language:
```
intreg comanda, a, b, s1
real x, y, s2
Citeste comanda
Daca comanda = 0 atunci

     Citeste a, b
     s1 <-- a + b
     Scrie s1

   altfel
     Citeste x, y
     s2 <-- x + y
     Scrie s2
```

In C++ programming language

```
  int comanda, a, b, s1;
  float x, y, s2;
  cin>>comanda;
  if(comanda == 0) {
        cin>>a>>b;
        s1 = a + b;
        cout<<s1;
  } else {
        cin>>x>>y;
        s1 = x + y;
        cout<<s2;
  }
```
5) Se citesc doua numere reale a si b. Sa se rezolve ecuatia de gradul 1: ax + b = 0
```python
```


6) Se citesc trei numere reale a, b si c. Sa se rezolve ecuatia de gradul 2: ax^2 + bx + c = 0
```python
```

7) Se considera doua puncte in plan, exprimate prin perechi de coordonate (x,y). Ele reprezinta centrele a doua cercuri de raza R1, respectiv R2. Sa se verifice daca cele doua cercuri sunt tangente interne, tangente externe, secante sau exterioare.

```python
def module(n):

    if n < 0:
        return -n
    else:
        return n

class Circle:
    def __init__(self,name,x,y,r):

        self.x = x#abscise
        self.y = y#ordonate
        self.r = r#radius
        self.name = name

    def __repr__(self):

        return "C%s(abs=%.2f,ord=%.2f,R%s=%.2f)"%(self.name,self.x,self.y,self.name,self.r)

def sqrt(n):
    x = n
    y = 1.0
    e = 0.000001
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    return x

def computeDistance(c1, c2):
    return sqrt((c2.y - c1.y) * (c2.y - c1.y) + (c2.x - c1.x) * (c2.x - c1.x))

def func():
    circle1 = Circle(1,5,9,11)
    circle2 = Circle(1,5,3,10)
    print(circle1)
    print(circle2)
    dist = computeDistance(circle1, circle2)
    print("%.3f"%dist)
    if dist > circle1.r + circle2.r:
        print("Exterior Circles.")
    elif dist == circle1.r + circle2.r:
        print("Tangent Exterior Circles.")
    elif dist < module(circle1.r - circle2.r):
        print("One circle is interior other one")
    elif dist == module(circle1.r - circle2.r):
        print("Interior tangent circles.")
    elif dist < circle1.r + circle2.r or dist < module(circle2.r - circle1.r):
        print("Secants")
func()
```

```c++
#include <stdio.h>

typedef struct circle {
        float x,
              y,
              R;
} Circle;

float module(float x) {
      if(x < 0) {
        return -x;
      } else return x;
}
float sqrt2(float n) {
      float x = n,
            y = 1,
            e = 0.000001;
      while(x - y > e){
            x = (x + y) / 2;
            y = n / x;
      }
      return x;
}
void read(Circle *c) {
     printf("abs = ");
     scanf("%f",&c->x);
     printf("ord = ");
     scanf("%f",&c->y);
     printf("R = ");
     scanf("%f",&c->R);
}

float computeDistance(Circle c1, Circle c2) {

      return sqrt2((c2.y - c1.y) * (c2.y - c1.y) + (c2.x - c1.x) * (c2.x - c1.x));
}

int main(int argc, char const *argv[]) {

  Circle c1,c2;
  float r1,r2;

  printf("Circle 1\n");
  read(&c1);

  printf("Circle 2\n");
  read(&c2);

  float distance = computeDistance(c1, c2);

  if(distance == c1.R + c2.R) {
     printf("Exterior Tangent Circles\n");
  } else if(distance > c1.R + c2.R) {
    printf("Exterior Circles\n");
  } else if(distance < module(c1.R - c2.R)) {
    printf("One Circle Interior\n");
  } else if(distance == module(c1.R - c2.R)) {
    printf("Interior Tangent\n");
  }
  return 0;
}

```

8) Realizati un program care verifica daca un punct X se afla din plan se afla in interioriul unui triunghi, pe laturile acestuia sau este exterior lui. Se cunosc coordonatele punctului si coordonatele varfurilor triunghiului.

```python
```
```c++
```

9) Se citesc de la intrare urmatoarele 5 numere reale: x, y, r, x0, y0 reprezentand coordonatele centrului unui cerc, raza sa si coordonatele unui punct din plan. Sa
se scrie un program care sa decida daca punctul (x0, y0) apartine interiorului, frontierei sau exteriorului cercului C(x0,y0,r).

```python
```
```c++
```

10) Se considera doua triunghiuri in plan, identificate prin coordonatele varfurilor lor. Sa se realizeze un program care verifica daca cele doua triunghiuri sunt asemenea.
```python
```
```c++
```
