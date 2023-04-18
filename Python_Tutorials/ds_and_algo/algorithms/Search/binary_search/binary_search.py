# Binary search faster than linear search. Half of the elements can be eliminated at a time, instead of
# eliminating them one by one.
# Restriction: Binary search only works for sorted arrays.
# Pseudocode: Create func with 2 parameters which are sorted array and value.
# Create 2 pointers: left pointer at start of array and right pointer at end of the array.
# Based on left and right pointer create middle pointer.
# While middle pointer is not equal to the value and start <= end loop:
#  (a) If the middle is greater than the value move the right pointer down.
#  (b)  If the middle is less than the value move the left pointer up.
# If value is never found return -1.
import math


def binary_search(arr, value):
    start = 0  # this is the start point
    end = len(arr) - 1  # to find end of array find len of array - 1

    middle = math.floor((start + end) / 2)

    while arr[middle] != value and start <= end:
        if value < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)

    if arr[middle] == value:
        return middle
    else:
        return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr1, 5))

