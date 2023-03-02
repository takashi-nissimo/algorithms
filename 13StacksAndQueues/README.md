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

### Results
```sh
(algorithms) $ python3 stack.py 
strings = ['to', 'be', 'or', 'not', 'to', '-', 'be', '-', '-', 'that', '-', '-', '-', 'is']
pops = ['to', 'be', 'not', 'that', 'or', 'be']
```

## Queue with two stacks

## Stack with max
Create a data structure that efficiently supports
the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are real numbers so that you can compare them.

### Results
```sh
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
