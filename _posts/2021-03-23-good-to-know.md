---
layout: post
disqus: n
title: Good to know Python 3
---

Here are things to keep in mind. Some of these you might have already inferred; others will show up as you learn Python.

- structure is defined by identation: no braces, no line ending semicolons, no begin or end symbols.
- to pack multiple statements on a line, separe them with semicolons(unless the first line ends with colon)
- to split long lines, use a backslash immediately before the line break, unless you are already inside a (), {}, or [] in which case breaks are always permitted.
- things are falsy: None, False, any numeric zero, any empty sequence, any empty mapping, instances of classes whose __nonzero__() or __len__() return 0 or False.
- tuples are immutable, lists are mutable
- the types you will probably use most often are: bool, int, float, str, complex, tuple, list, dict, function and NoneType.
- the built-in function help is super helpful in interactive mode.
