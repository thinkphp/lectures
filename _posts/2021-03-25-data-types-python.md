---
layout: post
disqus: n
title: Data Types Python
---

A data type is essentially an internal construct that a programming language uses to understand how to store and manipulate data. For instance needs to understand that you can add two numbers together like 5 + 5 to get 10, or if you have two strings such as 'dustin' and 'john' you could concatenate add them together to get to "dustinjohn".

Variables can store data of different types and different types can do different things.

Python has the following data types built-in by default, in these categories:

- text type: str
- numeric types: int, float, complex
- sequence types: list, tuple, range
- mapping type: dict
- set types: set, frosenset
- boolean type: bool
- binary types: bytes, bytearray, memoryview.

## Getting the Data Type:

```python

>>> type(8)
<class 'int'>
>>>type(2423542342356656575983745923479274923729399899898239443)
<class 'int'>
>>> type(False)
<class 'bool'>
>>> type(None)
<class 'NoneType'>
>>> type("Hello, how are you today?")
<class 'str'>
>>> type(2.77e6)
<class 'float'>
>>> type(3-3j)
<class 'complex'>
>>> type([4,5,6])
<class 'list'>
>>> type((9,4,'blue'))
<class 'tuple'>
>>>type({'CA':'Sacramento','HI':'Honolulu','AK':'Juneau'})
<class 'dict'>
>>> type(sum)
<class 'builtin_function_or_method'>
>>> type(lambda x: x * x)
<class 'function'>
>>> type(x for x in range(10))
<class 'generator'>
>>> int
<class 'int'>
>>> type(int)
<class 'type'>
```

### Setting the Data Type

In Python, the data type is set when you assign a value to a variable:

```python
v = "Hello world"
v = 9
v = 1.414243
v = 1j
v = ["car","air","house"]
v = ("car","air","house")
v = range(10)
v = True
v = False
v = {"name":"john", "country": "USA"}
```

### Setting the specific Data Type

```python
v = str("Hello world")
v = int(20)
v = float(1.42)
v = list(("tea","coffee","water"))
v = tuple(["tea","coffee","water"])
v = set(["tea","coffee","water"])
v = dict(name="John", age=36)
```
