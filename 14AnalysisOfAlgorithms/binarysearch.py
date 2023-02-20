from typing import Union


def binary_search(a: list, key: int, descend: bool = False) -> Union[int, None]:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        if descend:
            if a[mid] < key:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if a[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1


if __name__ == '__main__':
    a = list(range(-20, 20, 2))
    print(f'{a = }')
    print(f'{binary_search(a, -20) = }')
    print(f'{binary_search(a, 18) = }')
    print(f'{binary_search(a, 10) = }')
    print(f'{binary_search(a, 11) = }')
