from typing import TypeVar
from collections.abc import Iterable, Iterator
from random import randrange, choice, shuffle


class RandomizedQueue(Iterable[(Item := TypeVar('Item'))]):

    class RandomizedQueueIterator(Iterator[Item]):
        def __init__(self, randq: Iterable[Item]):
            shuffle(randq)
            self.randq = randq

        def has_next(self):
            return self.randq

        def __next__(self):
            if not self.has_next():
                raise Exception('NoSuchElementException')
            return self.randq.pop()

        def remove(self):
            raise Exception('UnsupportedOperationException')

    def __init__(self):
        """construct an empty randomized queue"""
        self.queue = []

    def is_empty(self) -> bool:
        """is the randomized queue empty?"""
        return not self.queue

    def size(self) -> int:
        """return the number of items on the randomized queue"""
        return len(self.queue)

    def enqueue(self, item: Item):
        """add the item"""
        if item is None:
            raise TypeError('NullPointerException')
        self.queue.append(item)

    def dequeue(self) -> Item:
        """remove and return a random item"""
        if self.is_empty():
            raise Exception('NoSuchElementException')
        return self.queue.pop(randrange(len(self.queue)))

    def sample(self) -> Item:
        """return a random item (but do not remove it)"""
        if self.is_empty():
            raise Exception('NoSuchElementException')
        return choice(self.queue)

    def __iter__(self) -> Iterator[Item]:
        """return an iterator over items in order from front to back"""
        return self.RandomizedQueueIterator(self.queue)


if __name__ == '__main__':
    randq = RandomizedQueue()
    items = list(range(6))
    [randq.enqueue(i) for i in items]
    print(f'{items = }  # enqueue in this order')
    print(f'{randq.sample() = },\t{randq.size() = }')
    print(f'{randq.sample() = },\t{randq.size() = }')
    print(f'{randq.dequeue() = },\t{randq.size() = }')
    print(f'{randq.dequeue() = },\t{randq.size() = }')

    try:
        iterator = randq.__iter__()
        print('iterator = randq.__iter__()')
        while True:
            print(f'{iterator.__next__() = }')
    except Exception:
        pass
