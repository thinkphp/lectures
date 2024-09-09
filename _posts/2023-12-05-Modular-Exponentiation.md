---
layout: post
disqus: y
title: Modular Exponentiation
---

```c++
typedef long long LL;
const LL MOD = 1000000007;  // You should replace this with the actual modulo value you want to use.

LL _pow(LL base, LL exp) {

    LL ans = 1;

    while (exp) {
        if (exp & 1) {
            ans = (ans * base) % MOD;
        }

        base = (base * base) % MOD;
        exp >>= 1;
    }

    return ans % MOD;
}
```

typedef long long LL;: This line creates an alias LL for the type long long, which is commonly used for representing large integers.

const LL MOD = 1000000007;: This line defines a constant MOD with a specific value (1000000007 in this case). You should replace this value with the actual modulo value you want to use.

The function _pow takes two parameters, base and exp, and calculates base^exp % MOD efficiently using binary exponentiation.

LL ans = 1;: Initializes the result variable ans to 1.

The while (exp) loop iterates until exp becomes zero.

Inside the loop:
if (exp & 1): Checks if the least significant bit of exp is set (i.e., if exp is odd). If true, it multiplies ans by base and takes the result modulo MOD.
base = (base * base) % MOD;: Squares the base value and takes the result modulo MOD. This is a key step in binary exponentiation.
exp >>= 1;: Right-shifts the bits of exp by 1, effectively dividing exp by 2.
The final result is ans % MOD to ensure the result is within the specified modulo range.

This function is particularly useful for calculating modular exponentiation efficiently, especially in scenarios where the result can be very large.
