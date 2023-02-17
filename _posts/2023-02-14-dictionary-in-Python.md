---
layout: post
disqus: n
title: Dictionary in Python
---

### Introduction

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values.

```python
dict = {
  "Venezuela": "Caracas",
  "Argentina": "Buenos Aires",
  "Chile": "Santiego"
}
print(dict)
```

### Building a Dictionary Incrementally

```
dict = {}
print(type(dict))
<class 'dict'>
dict["Venezuela"] = "Caracas"
dict["Philippines"] = "Manila"
dict["Argentina"] = "Buenos Aires"
dict["Chile"] = "Santiago"
```

### Access Items

You can access the items of a dictionary by referring to its key name, inside square brackets:

```python
print(dict["Philippines"])
print(dict.get("Philippines")
print(dict.keys())
print(dict.values())
print(dict.items())
```

### Loop dictionary

```python
for x in dict:
    print(x)

for x in dict:
    print(dict[x])

for x in dict.values():
    print(x)

for x in dict.keys():
    print(x)

for x,y in dict.item():
    print(x,y)    
```    
### Add Items

```python
```

### Update Items
You can change the value of a specific item by referring to its key name.
The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs.

```python
dict = {
  "Venezuela": "Caracas",
  "Argentina": "Buenos Aires",
  "Chile": "Santiego"
}
dict["Chile"] = "Manila"
dict.update({"Chile": "Manila"})
```

### Remove Items
```python
```

### Built-in Dictionary Methods
```python
```
