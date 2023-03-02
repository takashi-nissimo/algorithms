"""Stack with max.
Create a data structure that efficiently supports
the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are real numbers so that you can compare them."""

from typing import TypeVar
from decimal import Decimal

from stack import Stack


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
    stack = StackWithMax()
    numbers = (3.1, 4, 1, 5, 9)
    for n in numbers:
        stack.push(n)
        print(f'stack.push({n})\t\t{stack.max() = }')
    for _ in numbers[1:]:
        print(f'{stack.pop() = }\t{stack.max() = }')
