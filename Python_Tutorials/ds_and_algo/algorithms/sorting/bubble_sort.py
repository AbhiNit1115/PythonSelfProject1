# AKA Sinking Sort, we repeatedly compare each pair of adjacent items and swap  them if they are in the
# wrong order. When to use it:
# when the input is already sorted
# space is a concern
# easy to implement
# When Not to use:
# Average time complexity is poor


def bubble_sort(custom_list):
    for i in range(len(custom_list) - 1):
        for j in range(len(custom_list) - i - 1):
            if custom_list[j] >= custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    print(custom_list)
    print(custom_list[0], custom_list[-1])


arr = [2, -33, 12, 111, 1, 44, 55, 123, 23]
bubble_sort(arr)

