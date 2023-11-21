# given sequence of increasing numbers, return a sorted list of squares of those numbers
from typing import Union


def sort_square(array: Union[int, list]) -> Union[int, list]:
    last = len(array)
    left = 0
    right = last - 1

    result = [0] * last

    while left <= right:
        print(result)
        if abs(array[left]) > abs(array[right]):
            result[last - 1] = array[left] ** 2
            left += 1
        else:
            result[last - 1] = array[right] ** 2
            right -= 1
        last -= 1

    for i, num in enumerate(result):
        array[i] = num

    return array


nums = [-4, -2, -1, 0, 3, 5]
print(f"Initial list is: {nums}")

sort_square(nums)

print(f"Sorted list of squares is: {nums}")
