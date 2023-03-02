# Stacks and Queues
[Lecture Slides](https://www.coursera.org/learn/algorithms-part1/supplement/UAJbP/lecture-slides)

## Scripts
|file|algorithm|
|---|---|
|stack.py|Stack|
|queue_with_2stacks.py|Queue with two stacks|
|stack_with_max.py|Stack with max|
|deque.py|Deque (Double-Ended Queue)|
|randomized_queue.py|Randomized Queue|
|permutation.py|Permutation|

## Stack

### Stack test client
Read strings from standard input.
- If string equals "-", pop string from stack and print.
- Otherwise, push string onto stack.

### Results
```shell-session
(algorithms) $ python3 stack.py 
strings = ['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
pops = ['to', 'be', 'not', 'that', 'or', 'be']
```

## Queue with two stacks
Implement a queue with two stacks so that each queue operations takes a constant amortized number of stack operations.

### Results
```shell-session
(algorithms) $ python3 queue_with_2stacks.py 
items = (1, 0.5, 'abc', [1, 2, 3], None)  # enqueue in this order
queue.dequeue() = 1
queue.dequeue() = 0.5
queue.dequeue() = 'abc'
queue.dequeue() = [1, 2, 3]
queue.dequeue() = None
```

## Stack with max
Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are real numbers so that you can compare them.

### Results
```shell-session
(algorithms) $ python3 stack_with_max.py 
stack.push(3.1)         stack.max() = 3.1
stack.push(4)           stack.max() = 4.0
stack.push(1)           stack.max() = 4.0
stack.push(5)           stack.max() = 5.0
stack.push(9)           stack.max() = 9.0
stack.pop() = 9.0       stack.max() = 5.0
stack.pop() = 5.0       stack.max() = 4.0
stack.pop() = 1.0       stack.max() = 4.0
stack.pop() = 4.0       stack.max() = 3.1
```

## Deques and Randomized Queues
[specification](https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php)

### Deques Results
A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue
that supports adding and removing items from either the front or the back of the data structure.
```shell-session
(algorithms) $ python3 deque.py 
l_first = ['c', 'b', 'a']  # add_first in this order
l_last = ['x', 'y', 'z']  # add_last in this order
deque.size() = 6
deque.remove_first() = 'a'
deque.remove_last() = 'z'
deque.size() = 4
iterator = deque.__iter__()
iterator.__next__() = 'b'
iterator.__next__() = 'c'
iterator.__next__() = 'x'
iterator.__next__() = 'y'
```

### Randomized Queues Results
A randomized queue is similar to a stack or queue,
except that the item removed is chosen uniformly at random among items in the data structure.
```shell-session
(algorithms) $ python3 randomized_queue.py 
items = [0, 1, 2, 3, 4, 5]  # enqueue in this order
randq.sample() = 1,     randq.size() = 6
randq.sample() = 3,     randq.size() = 6
randq.dequeue() = 4,    randq.size() = 5
randq.dequeue() = 1,    randq.size() = 4
iterator = randq.__iter__()
iterator.__next__() = 5
iterator.__next__() = 2
iterator.__next__() = 3
iterator.__next__() = 0
```

### Permutation Results
Client program permutation.py that takes an integer k as a command-line argument;
reads a sequence of strings from standard input; and prints exactly k of them, uniformly at random.
Print each item from the sequence at most once.
```shell-session
(algorithms) $ python3 permutation.py 5 AA AO OA BB BO OB AB BA OO OO
OO
OA
OO
AB
OB
```
