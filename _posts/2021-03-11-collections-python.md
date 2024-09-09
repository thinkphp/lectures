---
layout: post
disqus: n
title: Collections Python
---

Earlier in this book we looked at some Python built-in types such as string,
int, float, bools and complex. These are not the only built-in types in Python;
another group of built-in types are collectively known as collection types.
This is because they represent a collection of other types (such as a collection
of string, or integers).

A collection is a single object representing a group of objects (such as a list or
dictionary). Collections may also be referred to as containers (as they contain other
objects). These collection classes are often used as the basis for more complex
or application specific data structures and data types.

These collection types support various types of data structures (such as lists and maps)
and ways to process elements within those structures. This chapter introduces
the Python Collection types.

There are four classes in Python that provides container like behaviour; that
is data types for holding collections of other objects, these are:

- Tuples
- Lists (Lists hold a collection of objects that are ordered and mutable/changeable
  they are indexed and allow duplicate members.
- Sets
- Dictionary

# Lists

Lists are mutable ordered containers of other objects. They support all the features
of the Tuples but they are mutable it is also possible to add elements to a List,
remove elements and modify elements. The element in the list maintain their order
(until modified).

## Creating lists

Lists are created using square brackets positined around the elements that make up
the list. For example:

list1 = ['John','Paul','George','Ringo']

In this case we have created a list of four elements with the first element
being indexed from ZERO, we thus have:

John   Paul  George   Ringo
0      1     2        3


As with Tuples we can have nested lists and lists containing different types
of elements. We can create the following structure of nested Lists:

- John    [1,3.14,'Person',True],   ['orange','apple',20] Ringo
- 0       1                         2                     3

In code this can be defined as:

```
l1 = [1,3.14,'Person',True]
l2 = ['orange','apple',20]
root_list = ['John',l1, l2, 'Ringo']
```

When the root_list is printed, we get:
['John',[1,3.14,'Person',True], ['orange','apple',20], 'Ringo']

Note the square brackets inside the outer square brackets indicating nested lists.
We can of course also nest Tuples in lists and lists in Tuples. For example, they
following structures shows Tuples (the ovals) hold references to Lists(rectangles)
and vice versa:

```
t1 = (1, 'John',3.14)
l1 = ['John','Diaz']
l2 = [t1, l1]
t2 = (l2, 'apple')
print(t2)
```
which produces:
- ([(1, 'John', 34.5), ['Smith', 'Jones']], 'apple')

### List Constructor Function

The List() function can be used to construct a list from an iterable; This
means that it can construct a list from a Tuple, a Dictionary or a Set. It can
also construct a list from anything that implements the iterable protocol.
The signature of the list() function is:

- list(iterable)


For example:

- vowelTuple = ('a','e','i','o','u')
- print(list(vowelTuple))

which produces:
- ['a','e','i','o','u']

### Accessing Elements from a List

You can access elements from a list using an index (within square brackets).
The index returns the object at that position, for example:

list1 = ['John','Paul','George','Ringo']
print(list1[1])

This will print out the element at index 1 which is Paul (lists are indexed from
ZERO si the first element is the zeroth element).

If you use a negative index such as -1 then the index is reversed so an index
of -1 starts from the end of the list (-1 returns the last element, -2 the second
to last, etc).

It is possible to extract a slice (or a sublist) from a list. This is done
by providing a starting and end end index to within the square brackets separated
by a colon. For example [1:4] indicates a slice starting at oneth element and
extending up to (but not including) the fourth element. If either of the indexes
is missed for a slice then that indicates the start or end of the list respective.

The following illustrates some of these ideas:

```
list1 = ['John','Paul','George','Ringo']
print('list1[1]:', list1[1])
print('list1[-1]:', list1[-1])
print('list1[1:3]:', list1[1:3])
print('list[:3]:', list1[:3])
print('list[1:]:', list1[1:])

#which produces:

list1[1]: Paul
list1[-1]: Ringo
list1[1:3]: ['Paul', 'George']
list[:3]: ['John', 'Paul', 'George']
list[1:]: ['Paul', 'George', 'Ringo']
```

### Adding to a list

You can add an item to a list using the append() method of the List class(this
changes the actual list; it does not create a copy of the list). The syntax of the
method is:

```
<alist>.append(<object>)
```

As an example, con  sider the following list of strings, to which we append a fifth
string:

```python
list1 = ['John', 'Paul', 'George', 'Ringo']
list1.append('Pete')
print(list1)
this will generate the output:
['John', 'Paul', 'George', 'Ringo', 'Pete']
```

You can also add all the items in a list to another list. There are several options
here, we can use the extend() method that will add the items passed to it to the
end of the list or we can use += operator which does the same thing:

```python
list1 = ['John', 'Paul', 'George', 'Ringo', 'Pete']
print(list1)
list1.extend(['Albert', 'Bob'])
print(list1)
list1 += ['Ginger', 'Sporty']
print(list1)
The output from this code snippet is:
['John', 'Paul', 'George', 'Ringo', 'Pete']
['John', 'Paul', 'George', 'Ringo', 'Pete', 'Albert', 'Bob']
['John', 'Paul', 'George', 'Ringo', 'Pete', 'Albert', 'Bob',
'Ginger', 'Sporty']
```

Which approach you prefer to use is up to you.
Note that strictly speaking both extend() and += take an iterable.

### Inserting into a list1

You can also insert elements into an existing list. This is done using the insert()
method of the List class. The syntax of this method is:

```
<list>.insert(<index>, <object>)
```

The insert() method takes an index indicating where to insert the element and an object to be
inserted.

For example, we can insert the string 'paloma' in between the Zeroth and oneth item
in the following list of names:

```
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)
#The result is:
['Adele', 'Madonna', 'Cher']
['Adele', 'Paloma', 'Madonna', 'Cher']
```

In other words, we have inserted the string 'Paloma' into the index position 1
pushing 'Madonna' and 'Cher' up one in the index within the List.

### List concatenation

It is possible to cancatenate two lists together using the concatenation operator
'+':

```
list1 = [3, 2, 1]
list2 = [6, 5, 4]
list3 = list1 + list2
print(list3)
#generates
[3, 2, 1, 6, 5, 4]
```

### Remove from a list

We can remove an element from a List using the remove() method. The syntax for this
method is:

```
<list>.remove(<object>)
```

This will remove the object from the list; if the object is not in the list, then
will generated an error by Python.


```
another_list = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_list)
another_list.remove('Robbie')
print(another_list)
#The output from this is:
['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
['Gary', 'Mark', 'Jason', 'Howard']
```

### The pop() Method

The syntax of the pop() method is:

a.pop(index=-1)

It removes an element from the List; however, it differs from the remove()
method in two ways:
- it takes an index which is the index of the item to remove from the list rather
than the object itself.
- the method returns the item that was removed as its result.

An example of using pop() method is given below:

```
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6)
print(list6.pop(2))
print(list6)
```

will generate:

- ['Once', 'Upon', 'a', 'Time']
- a
- ['Once', 'Upon', 'Time']

an overload of this method is just:

```
<list>.pop()
```

Which removes the last item in the list. For example:

```
list6 = ['Once', 'Upon', 'a', 'Time']
print(list6)
print(list6.pop())
print(list6)
```

with the output:

```
['Once', 'Upon', 'a', 'Time']
Time
['Once', 'Upon', 'a']
```

### Deleting from  list

It is possible to use the del keyword to delete elements from a list.

The del keyword can be used to delete a single element or a slice from a list.

To delete an individual element from a list use del and access the element via
its index:

```
my_list = ['A', 'B', 'C', 'D', 'E']
print(my_list)
del my_list[2]
print(my_list)
```

which outputs:

- ['A', 'B', 'C', 'D', 'E']
- ['A', 'B', 'D', 'E']

To delete a slice from within a list use the del keyword and the slice returned
from the list.

```
my_list = ['A', 'B', 'C', 'D', 'E']
print(my_list)
del my_list[1:3]
print(my_list)

```

which deletes the slice from index 1 up to index 3 (not including)

['A', 'B', 'C', 'D', 'E']
['A','D','E']



### List Methods

- append() adds an element at the end of the list.
- clear() removes all the elements from the list
- copy() returns a copy of the list
- count() returns the number of elements with specified value
- extend() adds the elements of the list, to the end of the current list
- index() returns the index of the first element with the specified value
- insert() adds an element at the specified position
- pop() removes an item at the specified position
- remove() removes an item with a specified value
- reverse() reverses the order of the list
- sort() sorts the list

# Tuples

Tuples, along with Lists, are probably one of Python most used container types. They will present in almost any non-trivial Python program.
Tuples are an immutable ordered collection of objects; that is each element in a tuple has a
specific position (its index) and that position does not change over time. Indeed, it is Not
possible to add or remove from the tuple once it
has been created.

## Creating tuples

Tuples are defined using parentheses around
the elements that makeup the tuple, for example:
* tup1 = (1,2,3,4,7)
This defined a new Tuple which is referenced by
the variable tup1. The tuple contain exactly 5
elements (in this case integers) with the first
element in the tuple having the index 0 and the
last element in the tuple (the integer 7) having the index 4. This is illustrates below:
1 2 3 4 7
0 1 2 3 4

## The tuple() Constructor function

The tuple() function can be used to create a new
tuple from an iterable. An iterable is something
that implements the iterable protocol. This means
that a new tuple can be created from a Set, a List, A dictionary (as these are all iterable types), or any type that implements the iterable
protocol. The syntax of the tuple() function is:
tuple(iterable)

list1 = [1,2,3,4]
tuple1 = tuple(list1)
print(tuple1)
that generates the output: (1,2,3,4)

## Accessing Elements of a Tuple

The elements of a tuple can be accessed using
an index in square brackets. The index returns
the object of that position, for example:


```
tup1 = (1, 3, 5, 7)
print('tup1[0]:\t',tup1[0])
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])
```

## Creating New Tuples from Existing Tuples.

It is also possible to return whatis known
as a slice from a Tuple. This is a new Tuple
which is comprised of subset of the original Tuple. This is done by providing the start and
end indexes for the slice, separated by a colon,
within the index square brackets. For example:
* print("tup1[1:3]:\t", tup1[1:3])

Which returns a new Tuple of two elements containing the elements from index 1 up to
element 3 but not including. Note that the original Tuple is not affected in any way
(remember its immutable so cannot be modified).
The output of above is thus:
tup1[1:3]: (3,5)
There are in fact numerous variations of the use
of the slicing indices. For example, if the first index is omitted it indicates that the slice should start from the beginning of the
tuple, while omitting the last index indicates
it should go to the end of the Tuple.

```
print('tup1[:3]:\t', tup1[:3])
print('tup1[1:]:\t', tup1[1:])
```

which generates:

```
tup1[:3]:
tup1[1:]:
(1, 3, 5)
(3, 5, 7)
```

You can reverse a Tuple using the ::-1 notation
again this returns a new Tuple and has no effect on the original Tuple:
```
print('tup1[::-1]:\t', tup1[::-1])
```

this thus produces:

```
tup1[::-1]:
(7, 5, 3, 1)
```

## Tuples can hold different Types

## Iterating over Tuples

## Tuple related Functions

## Check if an element exists

## Nested Tuples

## Things you can't do with Tuples

Its not possible to add and remove Elements
from a Tuple; they are immutable. It should
be particulary noted that none of the functions
or methods presented above actual change the
original tuple they are applied to; even those
that return a subset of the original Tuple actually return a new instance of the class Tuple
and have no effect on the original Tuple.

# Sets

## Introduction

A set Type is an unordered (unindexed) collection of immutable object that does not
allow duplicates.

## Creating a Set

A set is defined using curly brackets ('{}')

For example:
```
basket = {'apple','orange','apple', 'pear', 'orange','banana'}
print(basket)
{'banana', 'orange', 'pear', 'apple'}
```

When you run this code will show that apple
is only added once to the set. Note that
because the Set is unordered it is notpossible
to refer to elements of the set using an index.

## The set constructor function

AS with tuples  and lists Python provides a predefined function that can convert any iterable type into a Set. The function signature is:
set(iterable)

Given an iterable object, this function returns a new Set based on the values obtained from the iterable. This means that a Set can be easily created from a List, Tuple or a Dictionary, as well as any other data type that implements the iterable protocol. For example, the following code snippet converts a Tuple into a Set.

```
set1 = set((1,2,3))
print(set1)
# which print out:
# {1,2,3}
```

## Accessing Elements in a Set

Unlike lists it is not possible to access
elements from a Set via an index; this is
because they are unordered containers and thus
there are no indexes available. However, They
are iterable containers.

Elements of a Set can be iterated over using
the For statement:

```
for item in basket:
    print(item)
```
This applies the print function to each item
in the listin turn.


## Working with Sets

* Checking for Presence of an Element

You can check for the presence of an element
in a set using the in keyword, for example:

```
print('apple' in basket)
```

This will print True if `apple` is a member of
the set basket.

* Adding items to a Set

It is possible to add items to a set using
add() method:

```
basket = {'apple','orange','banana'}
basket.add('apricot')
print(basket)
# this generates: {'orange', 'apple', 'banana', 'apricot', 'pear'}
```

If you want to add more than one item to a Set
you canuse the update() method:

```
basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)
# generating:
# {'orange', 'apple', 'mango', 'banana', 'apricot', 'grapefruit'}
```

The argument to update can be a set, a list, a tuple or a dictionary. The method automatically
converts the paramenter into a set if it is not
already and then adds the value to the original set.

* Changing Items in a Set
It is not possible to change items already in a Set.

* Obtaining the Length of a set.

As with other collection/container classes;
you can find out the length of a set using the
len() function.

```
basket = {'apple', 'orange', 'apple', 'pear', 'orange',
'banana'}
print(len(basket)) # generates 4
```

* Obtaining the MAx and Min values in a set.

You can also obtain the maximum or minimum values
in a set using the max() or min() functions.
```
print(max(a_set))
print(min(a_set))
```

* Removing an Item

To remove an item from a Set, use the remove()
or discard() functions. The remove() function
removes a single item from a Set but generetes
an error if that item was not initialling the set. The remove function also removes a single item from a set but does not throw an error
if it was not initially present in the set.

```
basket = {'apple', 'orange', 'apple', 'pear', 'orange',
'banana'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)
```

This generetes:

```
{'pear', 'banana', 'orange', 'apple'}
{'pear', 'banana', 'orange'}
```

It is also a method pop() that can be used to remove an item (and return that item as a result of running the method); however it removes the last item in the set(although as a set is unordered you will not know which item that will be).

The method clear() is used to remove all elements from a Set.

```
basket = {'apple', 'orange', 'banana'}
basket.clear()
print(basket)
```

will print out: set() which is used to represent an empty set.


* Nesting Sets

It is possible to hold any immutable object within a set. This means that a set can contain  reference to a Tuple (as that is immutable). We can thus write:
```
s1 = {(1,2,3)}
print(s1)
```

This prints out:
```
{(1,2,3)}
```

However we cannot nest List or other sets within
a Set as these are not immutables types. The following would both generate a runtime error in Python:
```
# Can't have the following
s2 = { {1, 2, 3} }
print(s2)
s3 = { [1, 2, 3] }
print(s3)
```

However we can use Frozenset and nest these within sets. A Frozenset is exactly like a Set except that it is immutable(it cannot be modified) and thus it can be nested within a Set. For example:

```
# Need to convert sets and lists into frozensets
s2 = { frozenset ({1, 2, 3}) }
print(s2)
s3 = { frozenset ([1, 2, 3]) }
print(s3)

#this generates
{frozenset({1, 2, 3})}
{frozenset({1, 2, 3})}
```
* Set operations:

The Set container also supports set like
operations such as Union (|), intersection (&),
difference(-) and symmetric difference(^).
These are based on simple Set Theory.

Given the two sets:

1) The Union of two sets represents the combination
of all the values in the two sets:

```
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}

#this would print out:
# print('Union:', s1 | s2)
Union: {'apple', 'lime', 'banana', 'grapefruit', 'orange'}
```

2) The intersection of two sets represents the common values between two sets:

```
print('Intersection:', s1 & s2)
# this generates
#Intersection: {'banana'}
```

3) The difference between two sets is the set of values in the first set that are not in the second set:

```
print('Difference:', s1 - s2)
# Which produces the output:
# Difference: {'apple', 'orange'}
```

4) The Symmetric Difference represents all the unique values in the two sets (that is the inverse of the interesection)

```
print('Symmetric Difference:', s1 ^ s2)
#symmetric Difference: {'orange', 'apple', 'lime', 'grapefruit'}
```

In addition to the operators there are also
method versions:

- s1.union(s2) is the equivalent of s1 | s2
- s1.intersection(s2) is the equivalent s1 & s2
- s1.difference(s2) is the equivalent of s1 - s2
- s1.symmetric_difference(s2) is the equivalent of s1 ^ s2

# Dictionaries

## Introduction

A dictionary is a set of associations between
key and a value that is unordered, changable (mutable) and indexed. Pictorially we might view
a Dictionary as shown below for a set of countries and thei capital cities. Note that
in a Dictionary the key must be unique but the
values do not need to be unique.

```
key         values
Wales       Cardiff
England     London
Scotland    Edinburgh
Irland      Dublin
```

## Creating a Dictionary
A dictionary is created using curly brackets ('{}') where each entry in the dictionaryis a
key:value pair.

```
cities = {'Wales': 'Cardiff',
'England': 'London',
'Scotland': 'Edinburgh',
'Northern Ireland': 'Belfast',
'Ireland': 'Dublin'}
print(cities)
```

This creates a dictionary referenced by
the variable cities which holds a set of
key:value pairs for the capital cities of the UK
and Ireland. When this code is run we see:
```
{'Wales': 'Cardiff', 'England': 'London', 'Scotland':
'Edinburgh', 'Northern Ireland': 'Belfast', 'Ireland':
'Dublin'}
```

## The dict() Constructor function.
