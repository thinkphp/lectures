---
layout: post
disqus: y
title: Declaring Variables in Rust
---

# Declaring Variables in Rust

In Rust, you can declare variables in various ways:

## 1. Implicit Type Declaration

Rust deduces the type of a variable based on the assigned value. In the following example, Rust infers that `a` is of type `i32` because `10` is an integer, and `i32` is the default type for integer values:

```rust
let a = 10;
```

## 2. Explicit Type Specification

You can explicitly specify the type of a variable:

```rust
let a: i32 = 20;
```

Here, the type is explicitly defined as `i32` for variable `a`.

## 3. Adding a Type Suffix

You can append a type suffix to a numeric literal to specify its type explicitly:

```rust
let b = 20i32;
```

In this case, `20i32` explicitly defines `b` as an `i32`. This method ensures that Rust interprets the literal as the specified type.

## 4. Using a Digit Separator

Rust allows the use of an underscore (`_`) as a separator in numeric literals to improve readability:

```rust
let d = 20_000_i32;
```

The underscore does not affect the numerical value; it simply enhances readability, especially for large numbers.

By using these various methods, Rust provides flexibility and clarity when declaring variables.

## Fibonacci Function in Rust

The following function calculates the Fibonacci number at a given position `n`:

```rust
fn fibonacci(n: i32) -> i32 {
    if n == 0i32 {
        return 0i32;
    } else if n == 1i32 {
        return 1i32;
    }

    let mut a = 0i32;
    let mut b = 1i32;

    for _ in 2i32..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }

    b
}

fn main() {
    let n = 10i32;
    println!("Fibonacci({}) = {}", n, fibonacci(n));
}
```

### Explanation:
- If `n` is `0`, the function returns `0`.
- If `n` is `1`, the function returns `1`.
- Otherwise, it initializes two variables, `a` and `b`, with the first two Fibonacci numbers (`0` and `1`).
- It iterates from `2` to `n`, updating the values to calculate the Fibonacci sequence iteratively.
- Finally, it returns the `n`-th Fibonacci number.

## Printing the Fibonacci Sequence up to a Limit

The following function prints the Fibonacci sequence up to a given number `n`:

```rust
fn fibonacci_sequence(n: i32) {
    let mut a = 0i32;
    let mut b = 1i32;

    print!("Fibonacci sequence up to {}: {} {}", n, a, b);

    while a + b <= n {
        let temp = a + b;
        print!(" {}", temp);
        a = b;
        b = temp;
    }

    println!();
}

fn main() {
    let n = 50i32;
    fibonacci_sequence(n);
}
```

### Explanation:
- Initializes `a` and `b` as `0` and `1`, the first two Fibonacci numbers.
- Prints the initial values.
- Uses a `while` loop to generate and print Fibonacci numbers until the sum exceeds `n`.
- This efficiently prints all Fibonacci numbers up to `n`.
