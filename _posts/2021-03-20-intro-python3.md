---
layout: post
disqus: n
title: Introducere in Python 3
---

## Overview

- Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
- Python este un limbaj de scripting expresiv, dinamically typed, garbage collected, introspectable.
- are un module system pentru a face large-scale programming possible.
- are o sintaxa simpla pentru high-level types: tupluri, multimi, liste, dictionare
- este un limbaj de programare orientat obiect
- are o bogata librarie standard si un imens ecosistem pentru third party libraries.

## It s used for:
- web development server-side
- software development
- maths
- system scripting

## What can Python do?

- poate fi folosit pe un server pentru a crea aplicatii WEB
- poate sa fie folosit alaturi de alte aplicatii pentru a crea fluxuri de date - workflows
- sa se conecteze la databases (MySQL, Oracle, Postgres, Redis, MongoDB)
- sa citeasca si sa modifice files.
- sa manipuleze BIG DATA.

## Why Python?
- poate rula pe diferite platforme (Windows, Mac, Linux)
- are o sintaxa simpla similara cu limba engleza
- are o sintaxa care permite inginerilor software sa scrie cu putine linii de cod aplicatii.
- ruleaza pe un interpretor system, asta inseamna ca codul poate fi execut de indata ce este citit.
- poate fi privit intr-o maniera procedurala, functionala sau orientata obiect.

## Python Model Execution

Python nu este un limbaj precompilat aidoma celorlalte limbaje de programare C++, Java, Pascal, etc. ci un limbaj interpretat. Foloseste un model intermediar. Converteste programul plain text intr-un format pseudo machine code si acest cod este executat.

app.py  ----> Python interpreter.

a) verifica daca programul este valid si bine format
b) compileaza in mod dinamic intr-un limbaj intermediar
c) ruleaza versiunea intermediara

## Running Python Program.

Avem trei modalitati prin care putem rula un program Py:

a) in mod interactiv folosind un interpretor Python
b) stocam programul plain text intr-un file cu extensia .py si rulam cu comanda python3 file.py
c) putem sa rulam programul dintr-un IDE (Integrated Development Environment). Exemple: PyCharm

## Python Interactive using REPL

Python 3.8.6 (default, Jan 27 2021, 15:42:20)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```python

>>> 1 + 1
2
>>> 8 - 1
7
>>> 10 * 5
50
>>> 10 / 5
2.0
>>> 5 // 4
1
>>> 5 // 3
1
>>> -5 // 3
-2
>>> 5.0 // 3.0
1.0
>>> -5.0 // 3.0
-2.0
>>> 10.0 / 3
3.3333333333333335
>>> 7 % 3
1
>>> -7 % 3
2
>>> 2**3
8
>>> 1 + 4 * 5
21
>>> (1 + 4) * 5
25
>>> True
True
>>> False
False
>>> not True
False
>>> not False
True
>>> True and True
True
>>> True and False
False
>>> True + True
2
>>> True * 8
8
>>> False - 5
-5
>>> 0 == False
True
>>> 1 == True
True
>>> 2 == True
False
>>> -5 != False
True
>>> bool(0)
False
>>> bool(4)
True
>>> bool(-6)
True
>>> 0 and 2
0
>>> -5 or 0
-5
>>> 1 == 1
True
>>> 2 == 1
False
>>> 1 != 1
False
>>> 2 != 1
True
>>> 1 < 10
True
>>> 1 > 10
False
>>>
>>> 1 < 2 and 2 < 3
True
>>> 2 < 3 and 3 < 2
False
>>> 1 < 2 < 3
True
>>> 2 < 3 < 2
False
```
