---
layout: post
disqus: n
title: Operator Overloading Python
---

## Introduction

 We'll explore Operator Overloading:
- what it is
- how it works
- why we want it

Operator overloading allows user defined class to appear
to have a natural way of using operators such as: +,-,*,/,<,>,=
as well as logical operators such as & |
This leads to more succint and readable code as it is possible to
write code such as:
-   q1 = Quantity(1)
-   q2 = Quantity(2)
-   q3 = q1 + q2

It feels  more natural for both developers and those reading the code. The alternative would be to create methods such as add and write code such as:
- q1 = Quantity(1)
- q2 = Quantity(2)
- q3 = q1.add(q2)

## Implementing Operator Overloading

```python
class Quantity:

      def __init__(self, value):
          self.value = value

      def __add__(self, other):
           new_value = self.value + other.value
           return Quantity(new_value)

      def __sub__(self, other):
          new_value = self.value - other.value
          return Quantity(new_value)

      def __mul__(self, other):
          new_value = self.value * other.value
          return Quantity(new_value)

      def __str__(self):
          return "Quantity["+ str(self.value) +"]"

      def __eq__(self, other):
          return self.value == other.value

      def __gt__(self, other):
          return self.value > other.value

      def __ge__(self, other):
          return self.value >= other.value

      def __lt__(self, other):
          return self.value < other.value

      def __le__(self, other):
          return self.value <= other.value
def main():
    q1 = Quantity(10)
    q2 = Quantity(20)
    q3 = q1 - q2
    print(q1<q2)
main()
```

https://ideone.com/cQfVX5
