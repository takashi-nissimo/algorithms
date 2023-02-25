from typing import Generic, TypeVar


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
        item = self.first.item
        self.first = self.first.next
        return item


if __name__ == '__main__':
    string = 'to be or not to - be - - that - - - is'.split(' ')
    stack = Stack()
    while string:
        if (s := string.pop(0)) == '-':
            print(stack.pop())
        else:
            stack.push(s)
