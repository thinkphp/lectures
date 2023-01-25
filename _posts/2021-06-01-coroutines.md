---
layout: post
disqus: n
title: Coroutines in Python
---

Coroutines were introduced in Python 2.5 but are still widely misunderstood. Much documention introduces Coroutines by sayinbg that  they are very similar to Generators, however there is a fundamental difference Generators and Coroutines:

- generators are data producers.
- coroutines are data consumers.

That is coroutines consume data produced by something else; where as a generator produces a sequence of values that something else can process.

The send() function is used to send values to a coroutine. These data items are made available within the coroutine; which will wait for values to be supplied to it. When a value is supplied then some behaviour can be triggered. Thus, when a coroutine consumes a value it triggers some behavoir to be processed.

Part of the confusion between Generator and Coroutine using the next() or send(None) functions. This advances the Coroutine to the call to yield where it will then wait until a value is sent to it.

A coroutine may continue forever unless close() is sent to it. It is possible to pick up on the coroutine being closed by catching the GeneratorExit exception; you can then trigger sume shut down behaviour if required.

An example of a coroutine is given by the grep() function below:

```python
def grep(pattern):
    print('Looking for', pattern)
    try:
      while True:
          line = (yield)
          if pattern in line:
             print(line)  

    except GeneratorExit:
        print("Exiting the Co-routine")  
```

This coroutine will wait for input data. when data is sent to the coroutine, then the data will be assigned to the line variable. It will then check to see if the pattern used to initialize the coroutine function is present in the line; if it is it will print the line; it will then loop and wait for the next data item to be sent to the coroutine. If while it is waiting the coroutine is closed, then it will catch the GeneratorExit exception and print out a suitable message.

The grep() function coroutine is used below, notice that coroutine function returns a coroutine object that can be used to submit data:

```python
print('Starting')
# Initialise the coroutine
g = grep('Python')
# prime the coroutine
next(g)
# Send data to the coroutine
g.send('Java is cool')
g.send('C++ is cool')
g.send('Python is cool')
# now close the coroutine
g.close()
print('Done')
```

The output from this is:

```
Starting
Looking for Python
Python is cool
Exiting the Co-routine
Done
```
