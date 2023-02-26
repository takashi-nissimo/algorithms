from typing import Generic, TypeVar
from collections.abc import Iterable, Iterator


class Deque(Iterable[(Item := TypeVar('Item'))]):

    class Node(Generic[Item]):
        def __init__(self, item: Item):
            self.item = item
            self.next: self[Item] = None
            self.prev: self[Item] = None

    class DequeIterator(Iterator[Item]):
        def __init__(self, deque: Iterable[Item]):
            self.node: Deque.Node = deque.first

        def has_next(self) -> bool:
            return self.node is not None

        def __next__(self) -> Item:
            if not self.has_next():
                raise Exception('NoSuchElementException')
            item = self.node.item
            self.node = self.node.next
            return item

        def remove(self):
            raise Exception('UnsupportedOperationException')

    def __init__(self):
        """construct an empty deque"""
        self.first = self.last = None
        self.n = 0

    def is_empty(self) -> bool:
        """is the deque empty?"""
        return self.n == 0

    def size(self) -> int:
        """return the number of items on the deque"""
        return self.n

    def add_first(self, item: Item):
        """add the item to the front"""
        if item is None:
            raise TypeError
        if self.is_empty():
            self.first = self.last = self.Node(item)
        else:
            node = self.Node(item)
            node.next = self.first
            self.first.prev = node
            self.first = node
        self.n += 1

    def add_last(self, item: Item):
        """add the item to the back"""
        if item is None:
            raise TypeError('NullPointerException')
        if self.is_empty():
            self.first = self.last = self.Node(item)
        else:
            node = self.Node(item)
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.n += 1

    def remove_first(self) -> Item:
        """remove and return the item from the front"""
        if self.is_empty():
            raise Exception('NoSuchElementException')
        item = self.first.item
        self.first = self.first.next
        if self.first is None:
            self.last = None
        else:
            self.first.prev = None
        self.n -= 1
        return item

    def remove_last(self) -> Item:
        """remove and return the item from the back"""
        if self.is_empty():
            raise Exception('NoSuchElementException')
        item = self.last.item
        self.last = self.last.prev
        if self.first is None:
            self.first = None
        else:
            self.last.next = None
        self.n -= 1
        return item

    def __iter__(self) -> Iterator[Item]:
        """return an iterator over items in order from front to back"""
        return self.DequeIterator(self)


if __name__ == '__main__':
    deque = Deque()
    deque.add_first('b')
    deque.add_first('a')
    deque.add_last('y')
    deque.add_last('z')
    print(f'{deque.size() = }')
    print(f'{deque.remove_first() = }')
    print(f'{deque.remove_last() = }')
    print(f'{deque.size() = }')
    try:
        [print(f'{item = }') for item in deque]
    except Exception:
        pass
