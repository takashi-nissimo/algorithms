from typing import Union


def binary_search(a: list, key: int, way: int = +1) -> Union[int, None]:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (diff := a[mid] - key) == 0:
            return mid
        if diff * way > 0:
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
