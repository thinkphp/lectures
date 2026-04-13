---
layout: post
disqus: y
title: Collatz Conjecture 3n + 1 in Rust
---

### Time Complexity O(n) Space O(1)

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

   let mut input = String::new();
   
   io::stdin().read_line(&mut input).unwrap();
   
   let n: u64 = input.trim().parse().unwrap();
   
   collatz_sequence( n );
}
```


### Recursive Variant Time Complexity O(n) Space O(1)

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


