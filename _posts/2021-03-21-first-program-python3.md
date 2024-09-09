---
layout: post
disqus: n
title: First Program Python 3
---

## Ce este un algoritm?

### Definition1:

A set of instructions, or rules that, start with initial data, solves a class of problems using precise operations, executed mechanically, without creative human intervention.

To qualify as an algorithm, the set of instructions should have some properties:

- preciseness - or non-ambiguity. Each step must be non-ambiguous and executable without creative intervention.
- generality - it should solve a class of problems, not just one particular problem.
- finiteness - the algorithm must finish in a finite amount of time.
- correctness - the end result should be correct for all inputs.

A program is a sequence of instructions that specifies how to perform a computation. The computation might be something mathematical, such as solving a system of equations or finding the root of a polynomial, but it can also be a symbolic computation such as searching or replacing text in a document or something graphical, like processing an image or playing a video.

The details look different in different languages, buta few instructions appear in just about every language:

Input - get the data from keyboard, a file, the network, or some other device

output - display the data on the screen, save it in a file, sent it over the network

math - perform basic mathematical operations like addition or multiplication

conditional execution - check for certain conditions and run the appropriete code

repetition - perform some action repeatedly, usually with some variation.

Traditionally, the first program you right in a new language is called "Hello World!" because all it does is display the words "Hello worlds!". In Python it looks like
this:
```python
>>> print("Hello, world!")
```

This is an example of a print statement, althought it doesn t actually print anything on paper. It display a result on the screen. In this case, the result is the words: Hello, world!

The quotations marks in the program mark the beginning and the end of the text to be displayed; they do not appear in the result. The parentheses indicate that print is a function.

## Values and Types

A value is one the basic things a program works with, a letter or a number. Some values we have seen so far are 8, 23.34 and 'Hello, world!'

The values belong to different types:

- 8 is an integer
- 23.34 is a floating-point number
- 'hello world' is a string
If you are not sure what type a value has, the interpreter can tell you:

```python
>>> type(8)
<class 'int'>
>>> type(23.34)
<class 'float'>
>>> type('Hello, World!')
<class 'str'>
```

In these results, the word class is used in the sense of a category; a type is a category of values.

Not surprisingly, integers belong to the type int, strings to the type str and floating point numbers belong to the float type.

What about values like '8' and '23.3'. They look like numbers, but they are in the quotations marks like strings:

```python
>>> type('2')
<class 'str'>
>>> type('42.0')
<class 'str'>
```

## Interactive Hello world

The print() function actually tries to print whatever you give it:

- when it is given a string it will print a strings
- when it is given an integer such as 19, it will print 19
- when it is given a floating-point number such as 23.33 then will print 23.33

To run the program, if you are using an IDE such as Pycharm, then you can select the file in the left hand tree and from the right mouse button select Run.

If you are running it from the command line type the python3 followed by the name of the file, by example:

user@ubuntu: python3 filename.py

This should be done in the directory where you created the file.

Let's make our program a little more interesting; lets get it to ask us our name and say hello to us personally.

in your filename.py:

```python
print("Hello, world!")
user_name = input("Enter the name: ")
print("Hello, ", user_name)
```

Now after printing the original 'Hello world' string, the program has two additional statements.

The result of running this program is:
Hello, world!
Enter your name: John
Hello, John

We look at each of new statement separately:
user_name = input("Enter your name: ")

This statement does several things. It first executes another function called input(). This function is passed a string - which is known as a argument - to use when it prompts the user for input.

This function input() is a buit-in function that is part of the Python language. In this case it will display the string you provide as a prompt to the user and wait the user type something in followed by the return key. Whatever the user types in then returned as a result of executation the input() function. In this case that result is then stored in the VARIABLE user_name.

A variable is a named area of the computer s memory and can be used to hold things (often referred to as data) such as strings, numbers, boolean as True/False. In this case the variable user_name is acting as a label for an area of memory which will hold the string entered by the user. The basic idea is illustrated in the following  diagram:

user_name  ------------> 'john'

The variable user_name allows us to access this area of the memory easily and conveniently.

It is called a variable because the value it references in memory can vary during the lifetime a the program.

```python
print('Hello, world!')
name = input("Enter the name: ")
print("Hello, ", name)
name = input("What is the name of your best friend? ")
print("Hello best friend, ", name)
```

In Python the variable name is not restricted to holding a string such as 'john' and 'Diaz'; it can also hold other types of data as numbers or the values True and False. For example:

```python
my_variable = 'John'
print(my_variable)
my_variable = 40
print(my_variable)
my_variable = True
print(my_variable)
my_variable = 1.4142
print(my_variable)
```

As you can see my_variable first holds (or references the area of memory containing) the string 'John', it then holds the number 40, then holds the Boolean value True, and finally it holds the float-point number 1.14142.

This is referred to in Python as Dynamic Typing. That is the type of the data held by the variable can Dynamically change as the program executes.

One final aspect of the statement shown has yet to be considered:

my_variable = input("Enter your name: ")

What exactly is this '=' between the my_variable and the input() function?

it's called the assignment operator. It's used to assign the value returned by the function input() to the variable my_variable. It's probably the most widely used operator in Python.
