---
layout: post
disqus: n
title: Variables Python
---

Variables are containers for storing data values.

Python has no command for declaring a variable.

A variable is created at the moment you first assign a value to it.

## Variable Names

Rules for Python variables:
- a variable name must start with a letter or the underscore character
- a variable name cannot start with a number
- variable Names are case-sensitive.
- a variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, _)

```python
>>> 7a = 2
  File "<stdin>", line 1
    7a = 2
     ^
SyntaxError: invalid syntax
>>> more@ = 3
  File "<stdin>", line 1
    more@ = 3
          ^
SyntaxError: invalid syntax

>>> class = 2
  File "<stdin>", line 1
    class = 2
          ^
SyntaxError: invalid syntax
```


Example:
```python
# a is of type int
a = 10
# b is of type str
# string variables can be declared either by using
# single or double quotes
b = "George"
# c is of type str
c = 'Diaz'
# d is of type float
d = 1.414243
# we can assign the same value to multiple variables in one Line
x,y,z = "Hello"
#we can assign values to multiple variables in one line.
x,y,z = 1,2,3
```

## Casting

If you want to specify the data of a variable this can be done with casting:

```python
# a will be '3'
a = str(3)
# b will be 3
b = int(3)
# c will be 3.0
c = float(3)
```

## Get The type

```python
x = 10
y = 'get the type'
z = 1.4534
print(type(x))
print(type(x))
print(type(z))
```

## Output Variables

- print statement is used often to output variables.
- to combine both text and variable, python usesthe + character.
```python
x = "world! "
print("Hello, " + world)
```

## Assignment Statements

An assignment statement creates a new variable and gives it a value:

```python
>>> message = 'an assignment statement creates a new variable'
>>> n = 29
>>> pi = 3.14159265
```

This example makes three assignments. The first assigns
a string to a variable named message; the second gives the integer 28 to n; the third assigns the approximate value of PI to pi.

## Expressions and Statements

An expression is a combination of values, variables and operators. A value all by itself is considered an expression, and so is a variable, so the following are all legal expressions:

```python
>>>47
47
>>> n = 17
17
>>>n + 25
42
```

When you type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression, n has the value 17 and n + 25 has the value 42.

A statement is a unit of code that has an effect, like creating a variable or displaying a value.

```python
>>>n = 17
>>>print(n)
```

The first line is an assignment statement that gives a value to n. The second line is a print statement that displays the value of n.

## Order of operations

When an expression contains more than one operator, the order of evaluation depends on the order of operations. For mathematical operators, Python follows mathematical conventions.

- parantheses have the highest precedence and can be used to force an expression to evaluate in the order you want. (1 + 1) ** (2 + 2)
- exponentation has the highest precedence, so 1 + 2 ** 3 + 3
- multiplications and division have highest precedence than Addition and Substraction. 2 * 5 + 1 = 11

## String operations.

The operator '+' performs string concatenation, which means it joins the strings by linking them end-to-end.

```python
>>> a = "hello, "
>>> b = "World!"
>>>a + b
>>> "Hello, world!"
```

The operator "*" also works on string; it performs repetition. For example "Spam" * r is SpamSpamSpam

## Scope and Lifetime of variables

We have already defined several variables in the examples we have being working with this lectures. In practice, most of these variables have been
what are known as global variables. That is there are accessible anywhere in our programs. In this chapter we will look at local variables as defined within a function, at global variables and how they can be refereced within a function and finally we will consider nonlocal variables.

- Local variables.

- The global keyword.

- NonLocal variables.
