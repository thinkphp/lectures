---
layout: post
disqus: y
title: Collatz Conjecture 3n + 1 in Rust
---

### Iterative Version Time Complexity O(n) Space O(1)


```rust

use std::io;

fn collatz_sequence(mut n: u64) {
   
   print!("{} ", n);
   
   
   while n != 1 {
   
         if n % 2 == 0 {
         
           n /= 2;
            
         } else {
                  
           n = 3 * n + 1;        
         } 
         
         print!("{} ", n);
   }
    
}

fn main() {

   let mut input = String::new(); //creates an enpty mutable string that will store the user input
   
   io::stdin().read_line(&mut input).unwrap(); //reads a full line from standard input keyboard and store it in input
   //for example, if you type 23, then input becomes "23\n" including newline character,so input becomes 23
   
   let n: u64 = input.trim().parse().unwrap();
   //attempts to convert the trimmed string into a number type
   //specifies that the parsed valud should be interpreted as an unsigned 64-bit integer(u64)
   
   //unwrap() -> if parsing succeeds, it returns the numbers, otherwise if the parsing fails (e.g. input = "abc") the program will crash (panic)
   
   collatz_sequence( n );
}
```

### Recursive Version Time Complexity O(n) Space O(1)

```rust

use std::io;

fn collatz_recursive(n: u64) {

    print!("{} ", n);

    if n == 1 {
    
        return;
    }

    if n % 2 == 0 {
    
        collatz_recursive(n / 2);
        
    } else {
    
        collatz_recursive(3 * n + 1);
    }
}

fn main() {

    let mut input = String::new();
    
    io::stdin().read_line(&mut input).unwrap();
    
    let n: u64 = input.trim().parse().unwrap();

    collatz_recursive(n);
}
```

--


