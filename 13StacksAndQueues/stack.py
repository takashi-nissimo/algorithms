from abc import abstractmethod
from typing import Generic, TypeVar


class Stack(Generic[(Item := TypeVar('Item'))]):
    """Abstract Class for Stack"""
    @abstractmethod
    def push(self, item: Item):
        pass

    @abstractmethod
    def push(self) -> Item:
        pass


class LinkedListStack(Stack):

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


class ResizingArrayStack(Stack):

    def __init__(self):
        self.N = 1
        self.s = [None]

    def resize(self, capacity: int):
        if capacity > len(self.s):
            self.s = self.s + [None] * (capacity - len(self.s))
        else:
            self.s = self.s[:capacity]

    def push(self, item: Item):
        if self.N == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.N] = item
        self.N += 1

    def pop(self) -> Item:
        self.N -= 1
        item: Item = self.s[self.N]
        self.s[self.N] = None
        if self.N > 0 and self.N == len(self.s) // 4:
            self.resize(len(self.s) // 2)
        return item


def main(stack):
    print(f'* {stack.__class__.__name__}')
    strings = 'to be or not to - be - - that - - - is'.split(' ')
    print(f'{strings = }')
    pops = []
    while strings:
        if (s := strings.pop(0)) == '-':
            pops.append(stack.pop())
        else:
            stack.push(s)
    print(f'{pops = }')


if __name__ == '__main__':
    main(LinkedListStack())
    main(ResizingArrayStack())
