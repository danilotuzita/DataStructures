from datetime import datetime
import random

def is_sorted(array, comp) -> bool:
    last = None
    for item in array:
        if last:
            if comp(item, last) < 0:
                print(last, '>', item)
                return False
        last = item
    return True


def comp(a, b) -> int:
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def quick_sort_rec(array: list, comp) -> list:
    # print(len(array))
    if len(array) <= 2:
        return array

    mid = len(array) // 2# random.randint(0, len(array) - 1)
    left = []
    right = []
    for i in range(len(array)):
        if i == mid:
            continue
        if comp(array[i], array[mid]) >= 0:
            right.append(array[i])
        else:
            left.append(array[i])
    left.append(array[mid])
    left = quick_sort_rec(left, comp)
    left.extend(quick_sort_rec(right, comp))
    return left



unsorted = [random.randint(0, 999) for i in range(100000)]
start = datetime.now()
sort = quick_sort_rec(unsorted, comp)
end = datetime.now()
print(f'my qsort = {end - start}')
print(is_sorted(sort, comp))

start = datetime.now()
sort = sorted(unsorted)
end = datetime.now()
print(f'sorted = {end - start}')
print(is_sorted(sort, comp))


# print(sort)
