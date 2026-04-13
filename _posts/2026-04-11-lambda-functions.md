---
layout: post
disqus: y
title: Lambda Functions in c++11
---

### An introductory course — C++11 and beyond
> Covers: syntax | capture | STL algorithms | closures | best practices

---

## 1. What is a Lambda Function?

A lambda function (also called a lambda expression or anonymous function) is a function defined inline, without a name, exactly where it is needed. Introduced in C++11, lambdas are one of the most important modern features of the language.

Before lambdas, passing custom behaviour to algorithms required writing a separate named function or a functor (a class with `operator()`). Lambdas eliminate that boilerplate entirely.

**Without lambda (C++03)**
```cpp
// A separate comparator function was required
bool byLength(const std::string& a, const std::string& b) {
    return a.size() < b.size();
}

std::sort(words.begin(), words.end(), byLength);
```

**With lambda (C++11)**
```cpp
// The comparator lives right at the call site
std::sort(words.begin(), words.end(),
    [](const std::string& a, const std::string& b) {
        return a.size() < b.size();
    });
```

The second version is shorter, easier to read, and keeps the logic **exactly where it belongs**.

---

## 2. Syntax Breakdown

Every lambda expression has four parts, three of which are optional:

```cpp
[ capture ] ( parameters ) -> return_type { body }
```

| Part | Description |
|---|---|
| `[ capture ]` | Variables from the outer scope accessible inside the lambda. Required, but can be empty `[]`. |
| `( parameters )` | Input parameters, exactly like a normal function. Can be omitted if there are none. |
| `-> return_type` | The return type. Optional — the compiler deduces it automatically in almost all cases. |
| `{ body }` | The function body. Any valid C++ code. |

**Minimal examples**
```cpp
// Absolutely minimal — no capture, no params, deduced return
auto greet = [] { std::cout << "Hello!\n"; };

// With parameters
auto add = [](int a, int b) { return a + b; };

// With explicit return type
auto divide = [](double a, double b) -> double {
    if (b == 0.0) return 0.0;
    return a / b;
};
```

---

## 3. The Capture Clause

The capture clause `[ ]` determines which variables from the surrounding scope are available inside the lambda, and how they are passed in.

| Syntax | Meaning |
|---|---|
| `[]` | Nothing captured. The lambda cannot access any outer variables. |
| `[=]` | Capture everything by value (copy). The lambda gets its own copy of each variable. |
| `[&]` | Capture everything by reference. The lambda reads and writes the originals. |
| `[x]` | Capture only `x`, by value. |
| `[&x]` | Capture only `x`, by reference. |
| `[x, &y]` | `x` by value, `y` by reference. |
| `[=, &x]` | Everything by value, except `x` which is by reference. |
| `[this]` | Capture the `this` pointer (used inside class methods). |

**Capture by value vs. by reference**
```cpp
int x = 10;
int y = 20;

// By value — lambda gets copies; originals are unchanged
auto byVal = [x, y]() { return x + y; };
std::cout << byVal() << "\n";  // 30

// By reference — lambda modifies the original variable
auto byRef = [&x]() { x += 5; };
byRef();
std::cout << x << "\n";  // 15
```

> **Rule of thumb:** capture by **value** when the lambda outlives the variable (e.g. stored in a callback). Capture by **reference** for short-lived lambdas used immediately.

---

## 4. The `mutable` Keyword

By default, variables captured by value are `const` inside the lambda — you cannot modify them. The `mutable` keyword lifts this restriction, allowing the lambda to modify its local copy (not the original).

```cpp
int counter = 0;

// Without mutable — compile error: counter is const
// auto f = [counter]() { counter++; };

// With mutable — modifies the local copy only
auto f = [counter]() mutable {
    counter++;
    return counter;
};

std::cout << f() << "\n";       // 1
std::cout << f() << "\n";       // 2
std::cout << counter << "\n";   // 0  — original unchanged
```

---

## 5. Storing and Passing Lambdas

Lambdas can be stored in variables and passed around like any other value. There are two common approaches.

**`auto` — for local storage**
```cpp
auto multiply = [](int a, int b) { return a * b; };
std::cout << multiply(4, 5) << "\n";  // 20
```

**`std::function` — for flexible storage and passing**
```cpp
#include <functional>

// Store as a typed function object
std::function<int(int, int)> op;

op = [](int a, int b) { return a + b; };
std::cout << op(3, 4) << "\n";  // 7

op = [](int a, int b) { return a * b; };
std::cout << op(3, 4) << "\n";  // 12

// Pass a lambda to a function
void apply(std::function<int(int)> f, int val) {
    std::cout << f(val) << "\n";
}

apply([](int x) { return x * x; }, 6);  // 36
```

> **Note:** `auto` is faster (no overhead); `std::function` is necessary when the lambda must be stored in a class member, a container, or passed across translation units.

---

## 6. Lambdas with STL Algorithms

This is where lambdas truly shine. Every STL algorithm that accepts a callable becomes dramatically more readable with a lambda.

**`std::sort` — custom comparator**
```cpp
std::vector<int> v = {5, 2, 8, 1, 9};

// Descending order
std::sort(v.begin(), v.end(),
    [](int a, int b) { return a > b; });
// v = {9, 8, 5, 2, 1}
```

**`std::find_if` — find first match**
```cpp
std::vector<int> nums = {3, 7, 2, 9, 4};

auto it = std::find_if(nums.begin(), nums.end(),
    [](int n) { return n > 5; });

if (it != nums.end())
    std::cout << "First > 5: " << *it << "\n";  // 7
```

**`std::transform` — map over a vector**
```cpp
std::vector<int> nums = {1, 2, 3, 4, 5};
std::vector<int> squares;

std::transform(nums.begin(), nums.end(),
    std::back_inserter(squares),
    [](int n) { return n * n; });
// squares = {1, 4, 9, 16, 25}
```

**`std::copy_if` — filter elements**
```cpp
std::vector<int> nums = {1, 2, 3, 4, 5, 6};
std::vector<int> evens;

std::copy_if(nums.begin(), nums.end(),
    std::back_inserter(evens),
    [](int n) { return n % 2 == 0; });
// evens = {2, 4, 6}
```

**`std::accumulate` — reduce / fold**
```cpp
#include <numeric>

std::vector<int> nums = {1, 2, 3, 4, 5};

int sum = std::accumulate(nums.begin(), nums.end(), 0,
    [](int acc, int n) { return acc + n; });
// sum = 15
```

---

## 7. Closures — Lambda Returning Lambda

A closure is a lambda that captures its environment and returns another lambda. This is a powerful pattern for creating configurable, reusable function objects.

**Factory function example**
```cpp
// makeMultiplier returns a NEW lambda each time
auto makeMultiplier(int factor) {
    return [factor](int x) {
        return x * factor;  // factor is captured
    };
}

int main() {
    auto triple = makeMultiplier(3);
    auto byTen  = makeMultiplier(10);

    std::cout << triple(5)            << "\n";  // 15
    std::cout << byTen(5)             << "\n";  // 50
    std::cout << triple(byTen(2))     << "\n";  // 60
    return 0;
}
```

Each call to `makeMultiplier` creates an independent lambda with its own captured copy of `factor`. This pattern is the C++ equivalent of partial application in functional programming.

---

## 8. Recursive Lambda

A lambda cannot refer to itself by its own name inside its body — it does not have one. The solution is to use `std::function`, which allows the lambda to refer to a named variable.

```cpp
#include <functional>

std::function<int(int)> factorial = [](int n) -> int {
    return (n <= 1) ? 1 : n * factorial(n - 1);
};

std::cout << factorial(6) << "\n";  // 720
```

> **Important:** the variable `factorial` must be declared with `std::function`, not `auto`, because at the time the lambda is defined, its own type is not yet known.

---

## 9. Complete Example with `main()`

The following program demonstrates all major concepts in a single, self-contained example.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

auto makeAdder(int base) {
    return [base](int x) { return base + x; };
}

std::function<int(int)> factorial = [](int n) -> int {
    return (n <= 1) ? 1 : n * factorial(n - 1);
};

int main() {
    // 1. Basic lambda
    auto greet = []() { std::cout << "Hello, Lambda!\n"; };
    greet();

    // 2. Lambda with parameters
    auto add = [](int a, int b) { return a + b; };
    std::cout << "3+4=" << add(3, 4) << "\n";

    // 3. Capture by reference
    int counter = 0;
    auto inc = [&counter]() { counter++; };
    inc(); inc(); inc();
    std::cout << "counter=" << counter << "\n";  // 3

    // 4. std::sort with lambda comparator
    std::vector<int> v = {5, 2, 8, 1, 9, 3};
    std::sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";  // 9 8 5 3 2 1

    // 5. std::transform — squares
    std::vector<int> nums = {1, 2, 3, 4, 5};
    std::vector<int> sq;
    std::transform(nums.begin(), nums.end(), std::back_inserter(sq),
        [](int n){ return n * n; });
    for (int x : sq) std::cout << x << " ";
    std::cout << "\n";  // 1 4 9 16 25

    // 6. std::accumulate — sum
    int sum = std::accumulate(nums.begin(), nums.end(), 0,
        [](int acc, int n){ return acc + n; });
    std::cout << "sum=" << sum << "\n";  // 15

    // 7. Closure — lambda returning lambda
    auto add10 = makeAdder(10);
    std::cout << "add10(7)=" << add10(7) << "\n";  // 17

    // 8. Recursive lambda
    std::cout << "5!=" << factorial(5) << "\n";  // 120

    return 0;
}
```

**Expected output**
```
Hello, Lambda!
3+4=7
counter=3
9 8 5 3 2 1
1 4 9 16 25
sum=15
add10(7)=17
5!=120
```

---

## 10. Best Practices

- Use `auto` to store lambdas locally. Reserve `std::function` only when you need to store or pass them across boundaries.
- Prefer **specific captures** (`[x, &y]`) over blanket captures (`[=]`, `[&]`). Explicit captures make dependencies obvious.
- Avoid capturing `[&]` in lambdas that outlive the current scope — dangling references cause undefined behaviour.
- Keep lambda bodies **short**. If the body exceeds ~5 lines, consider extracting it into a named function.
- Use `mutable` sparingly. If you need to mutate a lot of state, a regular function or a functor is likely clearer.
- For **recursive lambdas**, always use `std::function` — `auto` cannot refer to itself.

---

## 11. Quick Reference

| Feature | Syntax / Example |
|---|---|
| Basic lambda | `auto f = []() { ... };` |
| With parameters | `auto f = [](int a, int b) { return a+b; };` |
| Explicit return type | `auto f = [](double x) -> double { return x; };` |
| Capture by value | `[x, y]` — copies of x and y |
| Capture by reference | `[&x, &y]` — references to x and y |
| Capture all by value | `[=]` |
| Capture all by reference | `[&]` |
| mutable | `[x]() mutable { x++; }` — modifies local copy |
| Store in std::function | `std::function<int(int)> f = [](int x){ return x; };` |
| Sort comparator | `std::sort(v.begin(), v.end(), [](int a, int b){ return a>b; });` |
| Transform | `std::transform(... [](int n){ return n*n; });` |
| Filter | `std::copy_if(... [](int n){ return n%2==0; });` |
| Reduce | `std::accumulate(... 0, [](int acc, int n){ return acc+n; });` |
| Closure factory | `auto make = [](int x){ return [x](int y){ return x+y; }; };` |
| Recursive lambda | `std::function<int(int)> f = [](int n){ return n<=1?1:n*f(n-1); };` |
