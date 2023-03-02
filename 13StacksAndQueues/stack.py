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
        if self.is_empty():
            raise Exception('NoSuchElementException')
        item = self.first.item
        self.first = self.first.next
        return item


if __name__ == '__main__':
    stack = Stack()
    strings = 'to be or not to - be - - that - - - is'.split(' ')
    print(f'{strings = }')
    pops = []
    while strings:
        if (s := strings.pop(0)) == '-':
            pops.append(stack.pop())
        else:
            stack.push(s)
    print(f'{pops = }')
