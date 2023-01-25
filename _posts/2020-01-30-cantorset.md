---
layout: post
disqus: y
title: Cantor set
---

Cantorset
----------

```kotlin

val height = 5
val width = 81

val matrix = Array(height) {CharArray(width){ '*' }}

fun cantor(start: Int, len: Int, index: Int) {
	 
	 val seg = len / 3

     if( seg == 0 ) return

     for(i in index until height) {

         for (j in start + seg until start + seg * 2) matrix[i][j] = ' '       
     }

     cantor(start, seg, index + 1)

     cantor(start + seg * 2, seg, index + 1)
}

fun main(args: Array<String>) {
	
	cantor(0, width, 1)

	matrix.forEach { println(it) } 
}
```

Demo:

[https://ideone.com/mVNpaS](https://ideone.com/mVNpaS)
