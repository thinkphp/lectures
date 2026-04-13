---
layout: post
disqus: y
title: Fibonacci Function in Rust
---

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
