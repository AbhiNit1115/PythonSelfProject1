# Divide the array into 2 parts sorted and unsorted array
# Take first element from the unsorted array i.e. from 0th index and find its correct position in sorted array.
# repeat until unsorted array is empty


def insertion_sort(custom_list, k):
    for i in range(1, len(custom_list)):  # i: 1
        key = custom_list[i]  # Key: 6
        j = i - 1  # j: i - 1 = 0
        while j >= 0 and key < custom_list[j]:
            # j >= 0 and 6 < 4 in this case "False" so loop will increment till 2nd and 3rd index and so on
            custom_list[j + 1] = custom_list[j]  # post which 2nd and 3rd index would swapped and so on
            j = j - 1
        custom_list[j + 1] = key
    print(custom_list)
    print(custom_list[k])


clist = [4, 6, 8, 1, 11, 45, 23, 56]
#        0  1  2  3   4   5   6   7
insertion_sort(clist, 3)
