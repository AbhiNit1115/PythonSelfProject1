# 1.) Constant Complexity: O(1) e.g. accessing a specific element in an array it doesn't matter what's the
# size of the array might be it will always take constant time to find the first element from the array.
list1 = [1, 2, 3, 4, 5]
print(list1[1])  # only finding a particular element

# 2.) Linear Complexity: O(N) here time complexity grows in direction proportion to the size of the input data
list2 = [1, 2, 3, 4, 5]
for element in list2:
    print(element)
# here as soon as the elements inside the list increases the time complexity increases as well. Basically,
# Larger Input = Greater Time. E.g. If we have to find 1 hear from a deck with only one card the time complexity
# would be "constant" but increase the no. of cards to 54 time complexity increases "linearly".

# 3.) Logarithmic Complexity: Using binary search we can find an element in a sorted array
list3 = [1, 2, 3, 4, 5]
for x in list3:
    for y in list3:
        print(x, y)
