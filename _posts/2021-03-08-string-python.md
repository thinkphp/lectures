---
layout: post
disqus: n
title: String Python
---

In Python a string is a series, or sequence, of character in order. In this definition a character is anything you can type on thekeyboard in one keystroke, such as a letter
'a', 'b', 'c' or a number '1','2','3' or a special characters such as '\','#','$' etc. a space is also a character, altough it does not have a visible representation.

It should also be noted that strings are immutables. Immutable means that once a string has been created it cannot be changed. If you try to change a string you will in fact create a new string, containing whatever modifications you made, you will not affect the original stringin anyway; for the most part you can ignore this fact but it beans that if you try to get a substring or split a string you must remember to store the result - you will see later in this chapter.

To define the start and the end of a string we have used the single quote character ' thus all of the following are valid string:
'hello'
'hello world'
'Hello, Alexander!'
'to be or not to be that is the question!'

We can also define an empty string which has no characters in it (it is defined as a single quote followed immediately by a second quote with no gap between them). This is often used to initialise or reset a variable holding a reference to a string, for example.

some_string = ''

## Representing Strings

As stated above, we have used single quotes to define the start and the end of a string, however in Python single or double quotes can be used to define a string, thus both of the following are valid:
'hello String'
"hello String"

In Python these forms are exactly the same, although by convention we default to using single quotes. This approach is often referred to as being more Pythonic (which implies it is more the convention used by experienced Python programmers), but the language does not enforce it.

You should note however, you cannot mix the two styles of start and the end strings, that is you cannot start a string with a single quote and end a string with a double quote, thus the following are both illegal in Python:
'Hello, String"
"Hello, String'

A third alternative is the use of triple quotes, which might at first seem a bit unwieldy, but they allow a string to support multi-line strings, for example:

```python
z = """
Welcome
   to the
       jungle!
"""
```
Which will print out:

Welcome
    to the
       jungle!

## What Type is String

It is often said that Python is untyped; but this is not strictly true - as was stated in an earlier chapter
it is a dinamically typed language with all data having an associated type.

The type of an item of data (such as a string) determines what it is legal to do with the data and what the effect of various actions will be. For example, what the offect of using a '+' operator is will depend on the types involved; if they are numbers then the plus operator will add them together; if however strings are involved then the strings will be concatenated (combinated) together.

It is possible to find out what type a variable currently holds using a built-in type() function. This function takes a variable name and will return the type of the data held by the variable, for example:
   my_variable = "Cube"
   print(type(my_variable))
   The result of executing of these two lines of code is the output:
   <class 'str'>

This is a shorthand for saying that what is held in my_variable is currently a class(type) of string (actually string is a class in Python supports idea from Object Oriented Programming such as classes and we will encounter them later in this chapter)

## What can you do with Strings?

In Python terms this means operations of functions are their available or built-in that you can use to work strings. The answer is that there are very many. Some of these are described in this section.

- String concatenation

You can concatenate two strings together with + operator (an operator is an operation or behaviour that can be applied to the types involved). That is you can takeone string and addit to another string to create a new third string:

```python
string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2  
print(string_3)
print("Hello" + " world!")
```
The output from this is:
Good day
Hello world!

Notice that the way in which the string is defined does not matter here, string_1 used single quotes but string_2 used double quotes; however they are both just strings.

- Length of the string

It can be sometimes useful to know how long a string is, for example if you are putting a string into a user interface you might need to know how much of the string
will be displayed within the field. To find out the length of the string you use len() function, for example:

print(len(string_3))

This will print out the length of the string currently being held by the variable string_3(in terms of the number of characters contained in the string).

- Accesing a Character

As a string is fixed sequance of characters, it is possible to use square brackets and an index  (or position) to retrieve a specific character from within a string. For example:

```python
my_string = 'Hello'
print(len(my_string[4]))
my_string2 = "world"
print(len(my_string2))
```

However, you should note that strings are indexed from ZERO! This means that the first character is in position 0, the second in position 1 etc. Thus stating [4] indicates that we want to obtain the fifth character in string, which in this case is the letter 'o'. This for of
indexing elements is actually quite common in programming languages and is referred to a zero based indexing.

- Accesing a subset of Characters

It is also possible to obtain a subset of the original string, often reffered to as a substring (of the original string). This can be done using the square brackets notation but
using a ":" to indicate the start end points of the sub string. If one of the positions is omitted then the start or end of the string is assumed (depending upon the omission), for example:

```python
my_string = "Welcome to the jungle!"
print(my_string[4]) #character at position 4
print(my_string[1:5]) #from position 1 to 5
print(my_string[:5]) #from start to 5
print(my_string[2:]) #from position 2 to the end
```
will generate:
o
elco
welco
lcome to the jungle!

As such my_string[1:5] return the substring containing the 2nd to 6th letters.
In turn my_string[:5] returned the substring containing the 1st to 6th letters
and my_string[2:] the substring containing 3rd to the last letters.

- Repeating Strings.

We can also use '*' operator with strings. In the case of strings this means repeat the given string a certain number of times. This generates a new string containing the original string repeated n number of times. For example:

```python
print("*" * 10)
print("Hello" * 10)
```

will generate:

**********
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello


- Splitting strings

A very common requirement is the need to split a string up into multiple separate
strings based on a specific character such a space or a comma.

This can be done with the split() function, that takes a string to used in
identifying how to split up the receiving string. For example:

```python
title = "Hello, world, George"
print('Source string: ', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))
```

This produces as output:
Source string: Hello, world, George
Split using a space
['Hello,','world,', 'George']
Split using a comma
['Hello',' world', 'George']

As you be seen from this the result generated is either a list of each word
in string or three strings as defined by the comma.

- Counting strings.

It is possible to find out how many time a string is repeated in another string.
This is done using the count() function for example:

```python
my_string = 'Count, the numberof spaces'
print("my_string.count(' '):", my_string.count(' '))
```

which has the output:
my_string.count(' '): 8
indicating that there are 8 spaces in the original string.

- Replacing strings:

- Finding substrings:

- Converting other types intro Strings:

- Comparing strings

- Other String Operations
## Hints on Strings
