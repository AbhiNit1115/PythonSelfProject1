# When we create an array, we:
# Assign it to a variable.
# Define the types of elements that it'll store
# Define its size( the max no. of elements)

from array import *

arr1 = array('i', [1, 2, 3, 4, 5])
print(arr1)

# Insert elements
arr1.insert(5, 6)  # here 5 is the index and 6 is the element that we want to insert
print(arr1)

# If we try to insert an element at the beginning or in the middle then the elements in tha array has to
# shift one position in right
arr1.insert(0, 0)  # earlier on 0th index 1 was present now 1 will shift one position right and so on
# in order to accommodate the newly inserted array
print(arr1)


# This is time consuming operation so it will take O(n) time complexity in case of inserting elements in
# the start of middle but in case of inserting at last index it'll take O(1) time complexity

# Traverse array
def traverse_array(arr):
    for i in arr:
        print(i)


# O(n) time complexity
traverse_array(arr1)


# Access elements of array
def accessing_elements(arr, index):
    if index > len(arr):
        print("Array out of bound")
    else:
        print(arr[index])


accessing_elements(arr1, 3)


# Search Array
def search_array(arr, value):
    for i in arr:
        if i == value:
            return arr.index(value)
    return "Element doesn't exists"


search_array(arr1, 0)
