# Step 1: Insert Data into Binary Heap Tree
# Extract Data from binary heap
# Binary Heap is a BT with special properties:
# - The value of any given node must be less than or equal to its children(min heap)
# - The value of any given node must be greater than or equal to its children(max heap)
# When we extract data from binary heap we can extract only from the parent element(root node) and after
# extracting from parent element(root node) the last element in the binary heap becomes the parent element.
# Again if after exchange positions if properties of binary heap is violated we call heapify method.
# FOr Binary heap the logic is: on the root node of Binary tree the value would always be minimum
# so we we extract this value, again next value that would come would be second min and so on hence we can
# sort like this.
# Best suited with array not works much with linked list
# Time Complexity: O(NlogN)

def heapfiy(custom_list, n, i):  # n: no of elements in the list, i: index of the list

    smallest = i  # initialize the smallest no. as the first index that comes from the parameter.
    l = 2 * i + 1  # find the left right child of this index using formula
    r = 2 * i + 2  # find the right child of this index using formula

    # find the smallest number as we have to put that as root node in heap tree
    if l < n and custom_list[l] < custom_list[smallest]:
        smallest = l  # Now check if the left child is smaller than the root then smallest is left child
    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r  # Now check if the right child is smaller than the root then smallest is right child

    if smallest != i:  # check if smallest no. is != root node which is i index swap smallest with root index
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapfiy(custom_list, n, smallest)


def heap_sort(custom_list, k):
    n = len(custom_list)
    # build our heap tree by rearranging the array elements
    for i in range(int(n / 2) - 1, -1, -1):  # each time we'll go -1 until we reach 0
        heapfiy(custom_list, n, i)

    for i in range(n - 1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapfiy(custom_list, i, 0)
    custom_list.reverse()
    print(custom_list[len(custom_list) - k])


clist = [56, 14, 7, 98, 32, 12, 11, 50, 45, 78, 7, 5, 69]
heap_sort(clist, 5)
print(clist)
