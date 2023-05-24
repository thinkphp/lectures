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

Here is another example of using the queue.PriorityQueue class to create a priority queue of tasks with different priorities:

```
import queue

# Create a priority queue
pq = queue.PriorityQueue()

# Put some tasks with different priorities
pq.put((2, "Clean the house"))
pq.put((1, "Study for exam"))
pq.put((3, "Watch a movie"))

# Get the tasks in order of priority
while not pq.empty():
priority, task = pq.get()
print(f"Priority: {priority}, Task: {task}")

Output:

Priority: 1, Task: Study for exam
Priority: 2, Task: Clean the house
Priority: 3, Task: Watch a movie
```
