from typing import Union

from binarysearch import binary_search


def search_bitonic_peak(a: list) -> int:
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > a[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_bitonic(a: list, key: int) -> Union[int, None]:
    peak = search_bitonic_peak(a)
    if key > a[peak]:
        return None
    elif key == a[peak]:
        return peak
    else:
        if (idx := binary_search(a, key, way=+1)) is not None:
            return idx
        if (idx := binary_search(a, key, way=-1)) is not None:
            return idx


if __name__ == '__main__':
    a = list(range(-10, 10, 2)) + list(reversed(range(-9, 11, 2)))
    print(f'{a = }')
    print(f'{search_bitonic(a, 1) = }')
    print(f'{search_bitonic(a, 2) = }')
    print(f'{search_bitonic(a, -9) = }')
    print(f'{search_bitonic(a, 10) = }')
