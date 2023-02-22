from typing import Generic, TypeVar
from collections.abc import Iterable, Iterator


class Deque(Iterable[Generic[(Item := TypeVar('Item'))]]):

    def __init__(self):
        """construct an empty deque"""
        pass
    
    def is_empty(self) -> bool:
        """is the deque empty?"""
        pass

    def size(self) -> int:
        """return the number of items on the deque"""
        pass

    def add_first(item: Item):
        """add the item to the front"""
        pass

    def add_last(item: Item):
        """add the item to the back"""
        pass

    def remove_first(self) -> Item:
        """remove and return the item from the front"""
        pass

    def remove_last(self) -> Item:
        """remove and return the item from the back"""
        pass

    def iterator(self) -> Iterator[Generic[Item]]:
        """return an iterator over items in order from front to back"""
        pass

    
if __name__ == '__main__':
    pass
