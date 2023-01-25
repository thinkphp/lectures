---
layout: post
disqus: n
title: Flow of Control IF statement Python
---

## Introduction

In this chapter we are going to look at the if statement in Python. This statement is used to control the flow of execution
within a program based on some condition. These conditions represent some choice point that will be evaluated to True or False. To perform this evaluation it is common to use a comparison operator (for example to check to see if the temperature is greater than some threshold). In many cases these comparisons need to take into account serveral values and in these situations logical operators can be used to combine two or more comparison expressions together. This chapter first introduces comparison and logical operators before discussing the if statement itself.

### Comparison operators

Before exploring if statements we need to discuss comparison operators. These are operators that return Boolean Values. They are key to conditional elements of flow of control statements such as if.

A comparison operator is an operator that performs some form of test and returns True or False.

These are operators that we usein everyday life all the time. For example, do I have enough money to buy lunch, or is this shoe in my size, etc. In Python there are a range of comparison operators represented by typically one or two characters. These are:

```
operator       Description
==  3 == 3     Tests if two values are equal.
!=  3 != 3     Tests if two values are not equal to each other.
<   3 < 3      test if the left hand value is less than righ hand.
>   3 > 6      test if the left hand value is greater than right hand.
<=  1 <= 33    test if the left hand value is less or equat than righ hand.
>=  1 >= 11    test if the left hand value is greater or equal than righ hand.
```

### Logical operators

In addition to comparison operators, Python also has logical operators. Logical can be used to combined Boolean expressions together. Typically, they are used with comparison operators to create more complex conditions. Again, we use every day for example we might consider whether we can afford an ice cream and whether we will be having our dinner soon, etc.

There are three logical operators in Python these are listed below:

```
Operator:   Description
and         Returns True if both left and right are True.
or          Returns True if either left or right is True.
not         Returns True if the value being tested is False.
```

## The If Statement

An If statement is used as a form of conditional programming; something you probably do every day in the real world. That is, you need to decide whether you are going to have a tea or coffee or to decide if you have toast or a muffin for breakfast. In each
of these cases, you are making a choice; usually based on some information such as I had coffee yesterday, so I will have tea today.
In Python such choices are represented programmaticaly by the If condition statement.
In this construct if some condition is True some action is performed, optionally it is not True some other action may be performed instead.

### Working with an If Statement

In its most basic from, the If statement is:

If <condition-evaluating-to-boolean>:
statement

Note that the condition must evaluate to True or False (or an equivalent value - see later in this chapter). If the condition is True then we will execute the indented statement.
Note this indentation, this is very important in Python, layout of the code is very very important in Python. Indentation is used to determine how one piece of code should be associated with another piece of code.

Let us look at a simple example:

```Python
num = int(input('Enter a number: '))
if num < 0:
   print(num, 'Is negative')
```

In this example, the user has input the number. If it is less than zero a message noting this will be printed to the user. IF the number is positive; then nothing will be output.
For example:
Enter a number: -1
-1 is negative

If we wish to execute multiple statements when our condition is True we can indent several lines; in fact all lines indented to the same level after the If statement will automatically be part of the If statement. For example:

```
num = int(input("Enter another number: "))
if num > 0:
   print(num, 'is positive')
   print(num, 'squared is: ', num * num)
print("bye")   
# If we now run this program and input 2 then we will see
Enter another number: 2
2 is positive
2 squared is 4
Bye
```
How ever if we enter the value -1 then we get
Enter another number:
Bye

Note that neither of the indented lines was executed.
This is because the two indented lines are associated with the If
statement and will only be executed if the Boolean condition evaluates returns True. However the statement print("Bye") is not part of the if statement; it is merely the next statement to executed after the If statement (and its associated print() statements) have finished.

### Else in an If Statement

We can also define an else part of an If statement; this is an optional element that can be run if the conditional part of the if statement return False. For example:

```
num = int(input('Enter yet another number: '))
if num < 0:
print('Its negative')
else:
print('Its not negative'
```

Now when this code is executed, if the number entered is less than zero then the first print() statement will be run otherwise(else) the second print() statement will be run. However, we are guaranteed that at least one(and at most one) if the print() statements will execute. For example in run 1 if we enter the value 1:
```
Enter yet another number: 1
Its not negative
```

And the run 2 if we enter the value -1
```
Enter yet another number: -1
Its negative
```


### The Use of Elif

### Nesting If Statements

## If Expressions

## A note on True and False

## Hints

One thing to be very careful of in Python is layout.

Unlike language such as Java and C# the layout of your program
is part of your program. It determines how statements are associated together and how flow of control elements such as if
statements effect which statements are executed.
Also be careful with the If statement and its use of the ":" character. This character is key in separating out the conditional part of the If statement from the statements that will be executed depending upon whether the condition is True or False.

## Online Resources

## Exercises
