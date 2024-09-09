---
layout: post
disqus: n
title: Numbers Python
---

# Introduction

In this chapter we will explore the different way that numbers can be represented by built-in types in Python. We will also introduce the Boolean type used to represent True and False. As part of this discussion we will also
look at both numeric and assignment operators in Python. We will conclude by introducing the special value known
as None.

## Type of Numbers

There are three types used to represent numbers in Python; these are integers types, floating points numbers and complex numbers.
This begs the quention why? Why we have different ways of representing numbers; after all humans can easily work with the number 4 and the number 4.0 and do not need
completely different approaches to writting them (apart from '.' of course).

This actually comes down to efficiently in terms of both the amount of memory needed to represent a number and the amount of processing power needed to work with the number. In essence integers are simpler to work with and can take up less memory than real numbers. Integers are whole numbers that do not need to have a fractional element. When two integers are added, multiplied or subtracted they will always generate another integer number.

In Python real numbers are represented as floating point numbers or floats. These can contain a fractional part (the bit after the decimal point). Computers can best work with integers(actually of course only really 1s or 0s). They therefore need a way to represent a floating point or real number. Typecally this involves representing the digits before and after the decimal point.

The term floating point is derived from the fact
that there is no fixed number of digits before and after the decimal point; that is, the decimal point can float.

Operation on floating point numbers such as addition, subtract, multiplication, etc, will generate new real numbers which must also be represented. It is also much harder to ensure that
the results are correct as potentially very small or very large fractional parts may be involved. Indeed, most floating-point numbers are actually
represented as approximations. This means that one of the challanges in handling floating-point numbers is in ensuring that approximations lead to resonable results. If this is not done appropriately, small discrepancies in the approximations can snowball to the point where the final results become meaningless.

As a result, most computer programming languages treat such as 4 as being different from real numbers such as 4.0000004.

Complex numbers are an extension of real numbers in which all numbers are expressed as a sum of a real part and an imaginary part. Imaginary numbers are real multiples of the imaginary unit (the square root of -1), where the imaginary part is often written in mathematics using an "i", while in engineering it is often written using a "j".

Python has built-in support for complex numbers, which are written using the engineering notation; that is the imaginary part with a j suffix, e.g. 3 + 3j.

## Integers.

All integers values, no matter how big or how small are represented by the integral type in Python. For example:
```
x = 1
print(x)
print(type(x))
x = 10000000000000000000000000001
print(x)
print(type(x))
# if this code is run then the output will show
# that both numbers are of type int
1
<class 'int'>
10000000000000000000000000001
<class 'int'>
```

## Converting to Ints.

It is possible to convert another type into an integer using int() function. For example, if you want to convert a String into an Int(assuming the string contains an integer number) then we can do this using the int() function

```python
total = int('100')
```

This can be useful when used with the input() function.

The input() function always returns a string. If you want to ask the user to input an integer number, then we will need to convert the string returned from the input() function into an int. We can do this by wrapping the call to the input() function in a call to the int() function, for exaple:

```python
age = int(input("Please enter your age:"))
print(type(age))
print(age)
# Running this gives:
Please enter your age: 21
<class 'int'>
21
```

The function int() can be used also to convert a floating-point number into an int, par example:

```
i = int(1.0)
```

## Floating-Point Numbers.

Real Numbers, or floating-point numbers, are represented in Python using the IEEE 754-double precision binary floating-point number format; for the most part you do not need to know this, but it is something you can look up and read if you wish.

The type used to represent a floating-point number is called float.

Python represents floating point number using a decimal point to separate the whole part from the fractional part of the number, for example:

```
exchange_rate = 1.84
print(exchange_rate)
print(type(exchange_rate))
# this produces output indicating that we are storing the number 1.84 as a floating point number.
```

## Converting to Floats

As with integers it is possible to convert other types such as an int or a string into a float. this is done using float() function.

```python
int_value = 1
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))

# the output from this code snippet is:
int value as a float: 1.0
<class 'float'>
string value as a float: 1.5
<class 'float'>
```

## Converting an Input String into a Floating Point Number.

As we have seen the input() function returns a string; what happens if we want the user to input a floating point number or real number? As we have seen above, a string can be converted into a floating point number using the float() function and therefore we can use this approach to convert an input from the user into a float:

```
exchange_rate = float(input("Please enter the exchange rate to
use: "))
print(exchange_rate)
print(type(exchange_rate))
#using this we can input the string 1.83 and convert it into a floating-point number.
Please enter the exchange rate to use: 1.83
1.83
<class 'float'>
```

## Complex Number

Complex Numbers are Python third type of built-in numeric type. A complex number is defined by a real part and an imaginary part and has the form a + bi (where a and b are real numbers and i is part imaginary)

a + bi

a = real part
b = imaginary part

The real part of the number (a) is the real number that is being added to the pure imaginary number.

The imaginary part of the number, or b, is the real number coefficient of the pure imaginary number.

The letter "j" is used in Python to represent the imaginary part of the number, for example:

```python
c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)

#We can run this code and the output will be:
c1: 1j , c2: 2j
<class 'complex'>
0.0
1.0
```

As we can see the type of the number is complex and when the number is printed directly is is done so by printing both the real and imaginary parts together. Do not worry if this is confusing; it is unlikely that you will need to use complex numbers unless you are doing some specific coding, for example within a scientific field.

## Boolean Values

Python supports another Type called Boolean; a boolean type can only be one of True or False(or something else). Note that these values are True(with the capital T) and False (with a capital F); true and false in Python are not the same thing and have no meaning on their own.

The equivalent of the int or float class for Boolean is bool.

The following example illustrates storing  the two Boolean values into a variable all_ok:

```python
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

#The output of this is:

True
False
<class 'bool'>
```

The Boolean type is actually a sub type of integer (but with only the values True and False) so it is easy to translate between the two, using the functions int() and bool() to convert from Booleans to Integers and vice versa. For example:

```Python
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
# which produces
1
0
True
False
```

You can also convert strings into Booleans as long as the strings contain either True or False (and nothing else). For example:

``` python
status = bool(input('OK to proceed: '))
print(status)
print(type(status))

# when we run this

OK to proceed: True
True
<class 'bool'>
```

## Arithmetic Operators

Arithmetics Operators are used to perform some form of mathematical operation such as addition, subtraction, multiplication and division. In Python these operators are represented using  by one or two characters. The following tables
summarises the Python arithmetic operators:

```
Operator  Description
+         Add left and right values together
-         Subtract right value from left value  
*         Multiple the left and right values
/         Divide the left value by the r value
//        Integer division (ignore any r)
%         Modulus - only returns any reminder
**        Exponent or power operator
          the left value raised to the power of the right
```

### Integer Operations

Two integers can be added together using +, for example 10 + 5.  In turn two integers can be subtracted (10 -5) and multiplied (10 * 4). Operations such as +, -, and * between integers always produce integers results.

This is illustrated below:

```python
home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))
# The output from this is:
25
<class 'int'>
40
<class 'int'>
3
<class 'int'>
```

However you may notice that we have missed out division with respect to integers, why is this? It is because it depends on which division operator you use as to what the returned type actually is.

For example, if we divide the integer 100 by 20 then the result you reasonably expect to produce might be 5; but is not, it is actually 5.0
```python
print(100/20)
print(type(100/20))
#The output is:
5.0
<class 'float'>
```

As you can see from this the typeof the result is float(that is floating point number). So why is this the case?
The answer is that division does not know whether the two integers involved divide into one another exactly or not(i.e. is there a reminder). It therefore defaultsto producing a floating point or real number which can have a fractional part. This is of course necessaryin some situations, for example if you divide 3 by 2;

```python
res1 = 3/2
print(res1)
print(type(res1))
# In this case 3 cannot be exactly divided  by 2, we might say
that 2 goes into 3 once with remainder; this is what is shown by Python
1.5
<class 'float'>
```

The result is that 2 goes into 3, 1.5 times with the type of the result being a float.
If you are only interested in the number of times 2 does  go into 3 and are happy to ignore the fractional part then there is an alternative version of the divide operator //. The operator is referred to as the integer division operator.

```python
res1 = 3//2
print(res1)
print(type(res1))
# which produces
1
<class 'int'>
```

But what if you are only interested in the remainder part of a division, the integer division operator has lost part? Well in this case you can use the modulus operation '%'. This operator returns the remainder of a division: for example:

```
print('Modulus division 4 % 2:', 4 % 2)
print('Modulus division 3 % 2:', 3 % 2)
# which produces:
Modulus division 4 % 2: 0
Modulus division 3 % 2: 1
```

A final integer operator we will look is the power operator that can be used to raise an integer by a given power, for example 5 to the power of 3. The power operator is "**", this is illustrated below:

```python
a = 5
b = 3
print(a ** b)
# which generates the number 125
```

### Negative Number Integer Division

It is worth just exploring what happens in integer and true division when negative numbers are involved. For example:

```Python
print('True division 3/2:', 3 / 2)
print('True division 3//2:', -3 / 2)
print('Integer division 3//2:', 3 // 2)
print('Integer division 3//2:', -3 // 2)
#
# The output from this is:
True division 3/2: 1.5
True division 3//2: -1.5
Integer division 3//2: 1
Integer division 3//2: -2
```

The first three of these might be exactly what you expect given
our earlier discussion; however, the ouput of the last example may seem a bit surprising, why does 3//2 generates 1 but -3//2 generates -2?

The answer is that Python always rounds the result of integer division towards minus infinity (which is the smallest negative number possible). This means it pulls the result of the integer division to the smallest possible number, 1 is smaller thatn 1.5, but -2 is smaller than -1.5.

### Floating Point Number Operators

We also have the multiple, add, subtract and divide operations available for floating point numbers. All of these operators produce new floating point numbers:

```Python
print(2.3 + 1.5)
print(1.5 / 2.3)
print(1.5 * 2.3)
print(2.3 - 1.5)
print(1.5 - 2.3)
# these statements produce the output given below:
3.8
0.6521739130434783
3.4499999999999997
0.7999999999999998
-0.7999999999999998
```
### Integers and Floating Point Operations

Any operation that involves both integers and floating point numbers will always produce a floating point number. That is, if one of the sides of an operation such as, add, subtract, multiply and divide is a floating point number then the result will be a floating point number. For example, given an integer 3 and the floating point number 0.1 If we multiple them together then we get a floating point number:

```python
i = 3 * 0.1
print(i)
#Executing this we get:
0.3000000000004
```

Which may or may not have been what you expected (you might have expected 0.3); however this hightlights the comment at the start of this chapter relating to floating point numbers being represented as an approximation within a computer system. If this was part of a larger calculation (such as the calculationof the amount of interest to be paidon a very large loan overa 10 year period) then the end result might well be out by a significant amount.
It is possible to overcome this issue using one of Python modules or libraries. For example, the decimal module provide the Decimal Class that will appropriately handle multiplying 3 and 0.1;


### Complex Numbers Operators

Of course you can use operators such as multiply, add, subtract, and divide with complex numbers. For example:
```python
c1 = 1j
c2 = 2j
c3 = c1 * c2
print(c3)
# You can run this code and the output will be:
(-2 + 0j)
```

You can also convert another number of a string into a complex number using complex() function. For example:

```
complex(1) # generates(1 + 0j)
```

In addition the math modules provides mathematical functions for complex numbers.


## Assignment Operators

In chapter 3. we briefly introduced the assignment "=" operator which was used to assign a value to a variable. There are in fact several different assignment operators that could be used with numerical values.

These assignment operators are actually referred to as compound operators as they combine together a numeric operation (such as add) with the assignment operator. For example, the += compound operator is a combination of the add operator and the = operator such that
```
x = 0
x += 1
# has the same behaviour as x = x + 1
# some developers like to use these compound operators as they are more concise to write and can be interpreted more efficiently by the Python interpreter.
The following table provides a list of the available compound operators.

operator Description
+=       add the value to the left-hand var  
         x +=1 equivalent x = x + 1
-=       subtract the value to the left-hand var
         x -= 1 equivalent x = x - 1
*=       multiple the left hand var by the value
         x *=2 equivalent x = x * 2
/=       divide the var value by the right val
          a /= 2 equivalent a = a / 2
//=      use integer division
          a //= 2 equivalent a = a // 2   
%=       apply modulus operator
          a %= 2 equivalent a = a % 2   
**=      apply power operator
         x **=2 equivalent x = x ** 2
```




## None Value

Python has a special type, the NoneType, with a single value, None;
This is used to represent null values or nothingness.
It is not the same as False or an empty string or 0; it is non-value. It can be used when you need to create a variable but you do not have an initial value for it. For example:

winner = None
You can then test for the presence of None using "is" and "is not", for example:
print(winner is None)

This will print out True if and only if the variable winner is currently set to None.

Alternatively you can also write:

print(winner is not None)

Which will print out True only if the value winner is not None.

Several examples using the value None and the "is" and "is not" operators are given below:

```
winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner)

# the output of this codesnippet is:
winner: None
winner is None: True
winner is not None: False
<class 'NoneType'>
Set winner to True
winner: True
winner is None: False
winner is not None: True
<class 'bool'>
```
