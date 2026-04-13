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


