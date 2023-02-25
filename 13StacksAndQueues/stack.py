"""Stack with max. Create a data structure that efficiently supports
the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are real numbers so that you can compare them."""

from typing import Generic, TypeVar
from decimal import Decimal


class Stack(Generic[(Item := TypeVar('Item'))]):

    class Node(Generic[Item]):
        item: Item
        next: Generic[Item]

    first: Node = None

    def is_empty(self) -> bool:
        return self.first is None

    def push(self, item: Item):
        oldfirst = self.first
        self.first = self.Node()
        self.first.item = item
        self.first.next = oldfirst

    def pop(self) -> Item:
        if self.is_empty():
            raise Exception('NoSuchElementException')
        item = self.first.item
        self.first = self.first.next
        return item


class StackWithMax(Stack[(Real := TypeVar('Real', int, float))]):
    _max: Real = None

    def max(self):
        if self.is_empty():
            raise Exception('NoSuchElementException')
        return float(self._max)

    def push(self, item: Real):
        item = Decimal(item)
        if self.is_empty():
            super().push(item)
            self._max = item
        elif item > self._max:
            super().push(2 * item - self._max)
            self._max = item
        else:
            super().push(item)

    def pop(self) -> Real:
        item = super().pop()
        if self.is_empty():
            self._max = None
            return float(item)
        elif item > self._max:
            _max = self._max
            self._max = 2 * _max - item
            return float(_max)
        else:
            return float(item)


if __name__ == '__main__':
    stack = Stack()
    print('*', stack.__class__.__name__)
    string = 'to be or not to - be - - that - - - is'.split(' ')
    print(string)
    while string:
        if (s := string.pop(0)) == '-':
            print(stack.pop())
        else:
            stack.push(s)

    stack = StackWithMax()
    print('\n*', stack.__class__.__name__)
    numbers = (3.1, 4, 1, 5, 9)
    print(f'{numbers = }')
    for n in numbers:
        stack.push(n)
        print(f'stack.push({n})\t\t{stack.max() = }')
    for _ in numbers[1:]:
        print(f'{stack.pop() = }\t{stack.max() = }')
