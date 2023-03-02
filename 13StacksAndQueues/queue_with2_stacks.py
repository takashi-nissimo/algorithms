"""Queue with two stacks. Implement a queue with two stacks so that
each queue operations takes a constant amortized number of stack operations."""


class Stack(list):
    """use list as stack"""
    push = list.append


class QueueWith2Stacks:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        while self.s1:
            self.s2.push(self.s1.pop())

        self.s1.push(x)

        while self.s2:
            self.s1.push(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            raise Exception('NoSuchElementException')

        return self.s1.pop()


if __name__ == '__main__':
    queue = QueueWith2Stacks()
    items = (1, .5, 'abc', [1, 2, 3], None)
    print(f'{items = }')
    [queue.enqueue(i) for i in items]
    [print(f'{queue.dequeue() = }') for _ in items]
