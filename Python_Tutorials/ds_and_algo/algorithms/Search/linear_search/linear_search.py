# In Linear search items are searched one by one its a.k.a. sequential search. Time: O(N), space: O(1)
# Use: in case of unsorted array, not in case of sorted array.

# Pseudocode: Create a func with 2 parameters which are array and value.
# Loop through the array and check if the current element is equal to the value.
# if the element is found return the index at which the element is found.
# if the value is not found return -1
import math


def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


arr = [4, 6, 8, 1, 11, 45, 23, 56]
print(linear_search(arr, 11))

