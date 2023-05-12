---
layout: post
disqus: y
title: Priority Queue Data Structure
---
Today we will learn about a new abstract data type(ADT) or collection called a priority queue. A priority queue is like a regular queue, except that the elements are enqueued with a given priority number attached to each one. When you dequeue an element later, the element with the lowest number as its priority(considered to be the most urgent element) is the one that is removed from the queue and returned.

Priority queues are useful for many applications such as scheduling jobs in an operating system, printer jobs queues, prioritizing paths to explore in a maze, AI algorithms, games, and more.

Here is a short example of code that uses a priority queue:
```
PriorityQueue<string> faculty;
faculty.enqueue("M",5)
faculty.enqueue("A",2)
faculty.enqueue("B",4)
faculty.enqueue("C",3)
while(!faculty.isEmpty()) {
  cout<<faculty.dequeue()<<endl;//A C B M
}
```
