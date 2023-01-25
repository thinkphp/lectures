---
layout: post
disqus: y
title: Generators
---

Generators
----------

In many cases it is not appropriate or possible to obtain all the data to be processed up front (for performance reasons, for memory reasons). Instead lazily creating the data to be iterated over based on some underlying dataset, may be more appropriate.

Generators are a special function that can be used to generate a sequance of values to be iterated over on demand (that is when the values are needed) rather produced up front.

The only thing that makes a generator a generator function is the use of the YIELD keyword (that was introduced in Python 2.3).

The yield keyword can only be used inside a function or a method. Upon its execution the function is suspended, and the value of the yield statement is returned as the current cycle value. If this is used witha for loop, then the loop runs once for this value. Execution of the generator function is then resumed after the loop has cycled once and the next cycle value is obtained.

The generator function will keep supplying values until it returns (which means that an infinite sequence of values can be generated).

## Defining a Generator function

A very simple example of a generator  function is given below. This function is called the gen_numbers() function:

```python
def gen_numbers():
    yield 1
    yield 2
    yield 3
```

This is a generator function as it has at least one yield statement (in fact it has three). Each time the gen_numbers() function is called within a for statement it will return one of the values associated with a yield statement; in this case the value 1, then value 2 and finally the value 3 before it returns (terminates).


## Using a Generator function in a For Loop.

We can use gen_numbers() function in a for loop statement as shown below:

Which produces 1, 2 and 3 as output:

```
for i in gen_numbers():
    print(i)
```

It is common for the body of a generator to have some form of loop itself. This loop is typically used to generate the values that will be yielded. However, as is shown above that is not necessary and here a yield statement is repeated three times.

Note that gen_numbers() is a function but it is a special functionas it returns a generator object.

This is a generator function returns a generator object which wraps up the generation of the values required but this is hidden from the developer.

 Generators (also called simple generators for historical reasons) are relatively new to Python,
 and are (along with iterators) perhaps one of the most powerful features to come along for years. However, the generators concept is rather advanced, and it may take a while before it "clicks" and you see how it works or how it would be useful for you. Rest assured that while generators can help you write really elegant code, you can certainly write any program you wish without a trace of generatos.

A generator is a kind of iterator that is defined with normal function syntax. Exactly how generators work is best known through example. Let's first have a look at how you make them and use them, and take a peek
under the hood.  

Making a generator
------------------

 Making a generator is simple; it's just like making a function. I'm sure you are starting to tire of the good old Fibonacci sequence by now, so let me do something else.

```python


def nthPrime(gen, n):

    for i in range(n-1):

        gen.next()

    return gen.next()

def genPrimes():

    yield 2
    yield 3

    n = 3
    while True:
        n += 2  
        if isPrime(n):
           yield n

def isPrime(n):

     if n<=1:
        return False

     elif n == 2:
        return True

     elif n == 3:
        return True

     else:
        d = 3
        while d*d <= n:
               if( n % d == 0):
                   return False
               d += 2        

        return True  

if __name__ == "__main__":

   if len(sys.argv) != 2:

      print "Usage: python nthPrimes_yield.py 10001"

      sys.exit()

   n = int( sys.argv[ 1 ] )

   print nthPrime(genPrimes(), n)
```
