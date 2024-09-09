---
layout: post
disqus: n
title: Essential Algorithms
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

22) Compute LCM(a, b)

```py
# lcm.py
# This program computes the lowest common multiple of two positive numbers
# @ by Adrian
#
def gcd(a, b):
    while a != b:
      if a > b:
         a = a - b
      else:
         b = b - a
    return a

def euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# method 1
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            break
        greater += 1
    return greater

# method 2
def lcm2(a, b):
    return (a * b) // euclid(a, b)

def func():
    a = 12
    b = 14
    r = lcm2(a, b)
    print("LCM(%d, %d) = %d" % (a, b, r))

func()

```

23) Salesman Travelling Problem
```c++
#include <stdio.h>
#define fin "salesman.in"
#define fout "salesman.out"
#define SIZE 100

int stack[100], level, nodes, startNode;
int matrix[SIZE][SIZE], edges;

void init() {
     stack[level] = 0;
}

int succ() {

    if(stack[level] < nodes) {
      stack[level]++;
      return 1;
    }else
    return 0;
}

int valid() {
    if(!matrix[stack[level-1]][stack[level]]) return 0;
    for( int i = 1; i < level; ++i ) {

        if(stack[i] == stack[level]) return 0;
    }

    return 1;
}

void print() {

     for(int i = 1; i <= nodes; ++i) printf("%d ", stack[i]);

     printf("\n");
}

int sol() {

  return level == nodes && matrix[startNode][stack[level]] == 1;
}

void back() {

     stack[ 1 ] = startNode;

     level = 2;

     init();

     while(level > 0) {
       int h = 1,
           v = 0;
       while(h && !v) {
         h = succ();
         if(h == 1) {
           v = valid();
         }
       }

       if(h) {
         if(sol()) {
           print();
         }else{
           level++;
           init();
         }
       } else
         level--;
       }
}

void readGraph() {

     int x, y;
     freopen(fin,"r", stdin);
     scanf("%d %d", &nodes, &edges);

     while(edges--) {
       scanf("%d %d", &x, &y);
       matrix[x][y] = 1;
       matrix[y][x] = 1;
     }
}

void displayGraph() {
     for(int i = 1; i <= nodes; ++i) {
       for(int j = 1; j <= nodes; ++j) {
         printf("%d ", matrix[i][j]);
       }
       printf("\n");
     }
}

int main(int argc, char const *argv[]) {

  readGraph();
  //displayGraph();
  startNode = 1;
  back();
  return 0;
}

```

```python
def init():

    stack[level] = 0

def succ():

    if stack[level]<nodes:
        stack[level]+=1
        return True

    return False

def valid():

    if matrix[stack[level-1]][stack[level]] == 0:
        return False

    for i in range(1, level):

        if stack[level]==stack[i]:

            return False

    return True

def sol():
    return level == nodes and matrix[startNode][stack[level]] == 1

def printf():
    for i in range(1,nodes+1):
        print(stack[i], end = " ")
    print()

def back():

    global level
    stack[1] = startNode
    level = 2
    init()
    while level > 0:
        h = True
        v = False
        while h is True and v is False:
            h = succ()
            if h is True:
                v = valid()
        if h is True:
            if sol() is True:
                printf()
            else:
                level+=1
                init()
        else:
            level-=1

def func():
    global stack,nodes, edges, matrix, startNode
    nodes = 6
    edges = 10
    data = [ [1,2],[1,6],[2,3],[2,5],[3,4],[3,5],[3,6],[4,5],[5,6],[6,1] ]
    matrix = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
    stack = [0] * (nodes+10)

    for edges in data:
        x, y = edges[0], edges[1]
        matrix[x][y] = 1
        matrix[y][x] = 1

    startNode = int(input("Start Node = "))
    back()
func()
```

22) Color Map

```python

def init():
    stack[level] = 1

def succ():
    if stack[level]<4:
        stack[level]+=1
        return True
    return False

def valid():
    for i in range(level):
        if stack[level] == stack[i] and matrix[i][level] == 1:
            return False
    return True

def sol():
    return level == nodes

def printf():
    for i in range(1,nodes+1):
        print(stack[i], end = " ")
    print()

def bk():
    global level
    level = 2

    while level > 0:
       h = True
       v = False
       while h is True and v is False:
             h = succ()
             if h is True:
                 v = valid()
       if h is True:
           if sol() is True:
               printf()
           else:
               level+=1
               init()
       else:
            level-=1


def displayGraph():
    for i in range(nodes):
        for j in range(nodes):
            print(matrix[i][j], end = " ")
        print()

def func():
    global stack,nodes, edges, matrix
    nodes = 5
    edges = 8
    data = [ [1,2],[1,4],[2,3],[2,5],[3,1],[3,5],[4,5] ]
    matrix = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
    stack = [0] * (nodes+10)

    for edges in data:
        x, y = edges[0], edges[1]
        matrix[x][y] = 1
        matrix[y][x] = 1
    displayGraph()
    stack[1] = 1
    bk()
func()
```
source: https://ideone.com/uc1KPA

23) A(n,k)

```c++
#include <stdio.h>
#define DIM 100

int stack[DIM],
    n,k;

int valid(int level) {

    for(int i = 1; i < level; i++) {

      if(stack[i] == stack[level]) {

        return 0;
      }
    }
    return 1;
}

void display_solution() {

      for(int i = 1; i <= k; ++i) {

          printf("%d ", stack[i]);

      }
      printf("\n");
}

void solve(int level) {

     if(level > k) {

        display_solution();

     } else {

       for(int i = 1; i <= n; ++i) {

           stack[ level ] = i;

           if(valid( level ))

              solve( level + 1 );
       }
     }
}

int main(int argc, char const *argv[]) {

  n = 4;
  k = 2;

  solve( 1 );

  return 0;
}
```

23) C(n,k) n choose k

```py
# https://www.cuemath.com/n-choose-k-formula/
# https://webpages.charlotte.edu/ghetyei/courses/old/S19.3166/pcv.pdf

def init():
    st[level] = st[level-1]

def sol():
    return level == k

def succ():
    if st[level] < n - k + level:
        st[level] += 1
        return True
    return False

def printf():
    out = ""
    for i in range(1, k + 1):
        out += str(st[i]) + " "
    print(out)

def valid():

    return True

def bk():
    global level
    level = 1
    init()

    while level > 0:

        next = True
        val = False

        while next is True and val is False:
            next = succ()
            if next is True:
                val = valid()
        if next is True:
            if sol() is True:
                printf()
            else:
                level += 1
                init()
        else:
            level -= 1


def func():
    global n, k, st
    n = 4
    k = 2
    st = [0] * (n + 1)
    bk()
func()

```

24) Partition of a number

C Language
```c++
#include <stdio.h>
#define SIZE 100

int stack[SIZE],
    n,
    level,
    sum;

void init() {
    if(level == 1) {
       stack[level] = 0;
    } else {
       stack[level] = stack[level-1] - 1;
    }
}

int succ() {

    if(stack[level] < n - sum) {
       stack[level]+=1;
       return 1;
    }
    else{
    sum -= stack[level-1];
    return 0;
    }
}

int sol() {
    return sum == n;
}

void print() {
    for(int i = 1; i <= level;++i) {
        printf("%d ", stack[i]);
    }
    printf("\n");
    sum = sum - stack[level];
}

int valid() {
   if(stack[level] <= n - sum) {
      sum = sum + stack[level];
      return 1;
   }
   return 0;
}

void solve() {
   level = 1;
   init();

   while(level>0) {
     int su, va;
     su = 1;
     va = 0;
     while(su && !va) {
           su = succ();
           if(su) {
             va = valid();
           }
     }
     if(su) {
       if(sol()) print();
       else  {
         level+=1;
         init();
       }
     } else
       level--;
   }
}

int main(int argc, char const *argv[]) {

  n = 5;
  solve();

  return 0;
}

Python Language
```python
def partition():
    global n, sum, stack
    sum = 0
    n = int(input("n="))
    stack = [0]*(n+1)

    def init(level):
        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1] - 1
    def succ(level) -> bool:

        global sum
        if stack[level] < n - sum:
            stack[level] +=1
            return True
        else:
            sum -= stack[level-1]
            return False

    def valid(level) -> bool:
        global sum
        if stack[level] <= n - sum:
            sum += stack[level]
            return True
        return False

    def sol(level) -> bool:
        return sum == n

    def printf(level):
        global sum
        for i in range(1, level+1):
            print(stack[i], end = " ")
        print()
        sum -= stack[level]

    def solve(level):
        init(level)
        while succ(level) is True:
            if valid(level) == True:
                if sol(level) == True:
                    printf(level)
                else:
                    solve(level+1)
    solve(1)
partition()
```

```python
def func():
    global s, n
    def init():
        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1]-1

    def succ():
        global s
        if stack[level] < (n - s):
            stack[level] += 1
            return True
        else:
            s = s - stack[level-1]
            return False

    def valid():
        global s
        if stack[level] <= n - s:
            s = s + stack[level]
            return True
        return False

    def printf():
        global s
        for i in range(1, level+1):
            print(stack[i], end = " ")
        s -= stack[level]
        print()

    def sol():
        return s == n

    def backtracking():
        global level, s
        s = 0
        level = 1
        init()
        while level > 0:
            h = True
            v = False
            while h is True and v is False:
                h = succ()
                if h is True:
                    v = valid()
            if h is True:
                if sol() is True:
                    printf()
                else:
                    level+=1
                    init()
            else:
                level-=1

    n = 4
    stack = [0] * (n+1)
    backtracking()

func()
```
Ruby Language
```ruby
def func

    def init
      if $level == 1
        $stack[$level] = 0
      else
        $stack[$level] = $stack[$level-1]-1
      end
    end

    def succ()
        if $stack[$level] < $n - $s
           $stack[$level] += 1
           return true
        else
           $s = $s - $stack[$level-1]
           return false
        end
    end

    def valid
        if $stack[$level] <= $n - $s
           $s = $s + $stack[$level]
           return true
        end
        return false
    end

    def sol
        return $s == $n
    end

    def printf
      for i in 1..$level
        print $stack[i], ' '
      end
      $s = $s - $stack[$level]
      print "\n"
    end

    def solve
      $s = 0
      $level = 1
      init()

      while $level > 0
            su = true
            v = false
            while su == true && v == false
                  su = succ()
                  if su == true
                    v = valid()
                  end
                  if su == true
                    if sol() == true
                       printf()
                    else
                      $level = $level + 1
                      init()
                    end
                  else
                    $level = $level - 1
                  end
            end
      end
    end

    $n = 5
    $stack = [0] * ($n+1)
    solve
end

func
```

Demos: https://ideone.com/mTFfYg

25) Permutation n!

C Language
```c++
#include <stdio.h>
#define DIM 100

int n, stack[DIM], explored[DIM];

void print_permutation() {
     for(int i = 1; i <= n; ++i) {
       printf("%d ", stack[i]);
     }
     printf("\n");
}

void perm(int level) {
     if(level > n) {
        print_permutation();
     } else {
       for(int i = 1; i <= n; ++i) {
         if(!explored[i]) {
           stack[level] = i;
           explored[i] = 1;
           perm(level+1);
           explored[i] = 0;
         }
       }
     }
}

int main(int argc, char const *argv[]) {

  n = 3;
  perm(1);

  return 0;
}

```
Python Language
```python
#Problem: https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/0

class Solution:

    def find_permutation(self, S):

         L = list( S )

         out = [ ]

         n = len( L )

         out = []

         L.insert(0,0)

         stack = [ 0 ] * ( n + 1 )

         def sort(arr):

             n = len(arr)
             for i in range(1, n):
                 aux = arr[i]
                 j = i - 1
                 while j>=0 and aux < arr[j]:
                     arr[j+1] = arr[j]
                     j-=1
                 arr[j+1] = aux

         def solution():

             string = ""

             for i in range(1, n + 1):

                   string += L[stack[i]]

             out.append(string)


         def ok(level):

            for i in range(1, level):

                 if stack[i] == stack[level]:

                     return False

            return True

         def solve(level):

             if level > n:

                 solution()

             else:

                 for i in range(1, n+1):

                     stack[level] = i

                     if ok(level) is True:

                         solve(level+1)
         solve(1)
         out = [*set(out)]
         sort(out)
         return out

ob = Solution()

for i in ob.find_permutation("ABC"):

    print(i, end = " ")

```

```c++
#include <stdio.h>
#define DIM 100

int stack[DIM],
    n;

int valid(int level) {

    for(int i = 1; i < level; i++) {

      if(stack[i] == stack[level]) {

        return 0;
      }
    }
    return 1;
}

void display_solution() {

      for(int i = 1; i <= n; ++i) {

          printf("%d ", stack[i]);

      }
      printf("\n");
}

void solve(int level) {

     if(level > n) {

        display_solution();

     } else {

       for(int i = 1; i <= n; ++i) {

           stack[ level ] = i;

           if(valid( level ))

              solve( level + 1 );
       }
     }
}

int main(int argc, char const *argv[]) {

  n = 5;

  solve( 1 );

  return 0;
}
```

```py
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
def init():
    st[level] = 0

def succ():
    if st[level] < n:
        st[level] += 1
        return True
    else:
        return False

def valid():
    for i in range(1, level):
        if st[level] == st[i]:
            return False
    return True

def sol():
    return level == n

def printf():

    output = ""

    for i in range(1, n+1):

        output += str(st[i]) + " "

    print(output)

def bk():

    global level
    level = 1
    init()

    while level > 0:

        next = True
        Valid = False

        while next is True and Valid is False:
            next = succ()
            if next is True:
               Valid = valid()

        if next is True:
            if sol() is True:
                printf()
            else:
                #increase the level with 1 unit
                level += 1
                init()
        else:
            #decrease the level
            level -= 1
def main():
    global n, st
    n = 4   
    st = [0] * (n+1)
    bk()
    print(fact(n))
main()
```

26) Subsets of a set
```py
def func():
    def subset(working_set, k, n):
    	if k == n:
    	   s = {k for k in working_set if working_set[k] == 1}
    	   solutions.append(s)
    	else:
    		k+=1
    		for i in [0,1]:
    			working_set[k] = i
    			print(working_set)
    			subset(working_set, k, n)
    global solutions
    solutions = []
    n = 3
    subset({}, 0, n)
    print(solutions)
func()    	
```

Geometry

```
26) Sa se verifice daca doua drepte sunt paralele. Se
considera ca prima dreapta trece prin punctele A si B, iar cea de-a doua dreapta trece prin punctele C si D.

```python
class Point:
    def __init__(self, x, y):

        self.x = x
        self.y = y

def vertical(point1, point2):

    return abs(point1.x - point2.x) < 0.00001

def computeSlope(A, B):

    return (B.y - A.y ) / (B.x - A.x)

def parallel( point1, point2, point3, point4 ):

    if vertical(point1, point2) is True:

        if vertical(point3, point4) is True:
           print("Parallel with Axe Oy")
           return True

    return abs(computeSlope(point1, point2) - computeSlope(point3, point4)) < 0.00001

def func():

    point1 = Point(5,7)
    point2 = Point(1,3)
    point3 = Point(7,1)
    point4 = Point(9,3)

    if parallel(point1, point2, point3, point4) is True:

        print("The lines are parallels.")

    else:
        print("The lines are not parallels.")
func()

```

input: A(3,7), B(3,2); C(5,6); D(5,1)
output: Dreptele sunt paralele

input: A(4,4), B(11,11); C(9,4); D(14,9)
output: Dreptele sunt paralele pentru ca au pante egale.

27) Ecuatia carteziana a unei drepte este: ax+by+c=0.
Sa se determine coeficientii a, b si c ai dreptei, stiind
doua puncte M1(x1,y1) si M2(x2,y2) care determina dreapta.

Input: M(13, 5) N(7,17).
Output: a = -12, b = -6 and c = 186;

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def computeCoefs(A, B):

    global a, b, c
    a = A.y - B.y
    b = B.x - A.x
    c = (B.x * A.y) - (A.x * B.y)

def func():
    global a, b, c

    A = Point(13, 5)
    B = Point(7, 17)

    computeCoefs(A, B)

    print("a=%.2f\nb=%.3f\nc=%.3f;"%(a, b, c))
    print("Equation Line: %.2f x + %.2f y + %.2f = 0;"%(a, b, c))

func()
```

28) Sa se defineasca o functie logica pentru verificarea
coliniaritatii a trei puncte date si apoi sa se apeleze
functia definita in cadrul unui program.

```python
def module(n):
    if n < 0:
        return -n
    else:
        return n

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computeArea(A,B,C):
    area = A.x*(B.y-C.y) + B.x *(C.y - A.y) + C.x*(A.y - B.y)
    area = module(area)/2
    return area
def func():
    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)

    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)

    if area == 0.0:
        print("The points are collinears.")
    else:
        print("The points are not collinears.")
func()
```

Input: A(4,4) B(1,1,) C(7,7).
Output: punctele sunt coliniare.

29) Distanta de la un punct la o dreapta. Se dau o dreapta precizata prin punctele a doua puncte si un punct. Sa se defineasca o functie care furnizeaza distanta de la punct la dreapta.

input: A(11,11) B(4,4) Pc(2,12)
output: dist(p,d) = 7.07

```c++
#include <stdio.h>

typedef struct point {

    float x,  //abscise
          y;  //ordonate
} Point;

Point A, B, //line
P;//point
//coefs
float a, b, c;

float module(float n) {
      if(n<0){
        return -n;
      } else{
        return n;
      }
}

float sqrt2(float n) {
      float x = n,
            y = 1,
            e = 0.000001;
      while(x - y > e) {
        x = (x + y) / 2;
        y = n / x;
      }
      return x;
}

float computeCoefs(void) {

   a = A.y - B.y;
   b = B.x - A.x;
   c = (B.x * A.y) - (A.x * B.y);
}

void readPoint(Point*a) {

     printf("Abs=");
     scanf("%f", &a->x);
     printf("Ord=");
     scanf("%f", &a->y);
}

float distance(void) {

  return module((a*P.x+b*P.y+c)/sqrt2(a*a+b*b));
}

int main(int argc, char const *argv[]) {

  readPoint(&A);
  readPoint(&B);
  readPoint(&P);
  printf("A(%.2f,%.2f)\n",A.x,A.y);
  printf("B(%.2f,%.2f)\n",B.x,B.y);
  printf("Point(%.2f,%.2f)\n",P.x,P.y);
  computeCoefs();
  printf("a=%.2f b=%.2f c=%.2f\n", a, b, c);
  float dist = distance();
  printf("d(line, Point) = %.2f", dist);
  return 0;
}

```

30) Sa se defineasca o functie care furnizeaza aria unui triunghi precizat prin coordonatele varfurilor sale.

Input: A(2,2) B(2,8) C(13,2)
Output: 33

```python
def module(n):
    if n < 0:
        return -n
    else:
        return n

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computeArea(A,B,C):
    area = A.x*(B.y-C.y) + B.x *(C.y - A.y) + C.x*(A.y - B.y)
    area = module(area)/2
    return area
def func():
    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)
    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)
    print(area)
    print(area2)
func()
```
