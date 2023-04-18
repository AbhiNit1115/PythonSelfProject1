# When to use quick sort:
# When average expected time is O(NlogN)
# Avoid: When space is a problem
# When you need stable sort.

def partition(custom_list, low, high):
    i = low - 1
    pivot = custom_list[high]

    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i + 1], custom_list[high] = custom_list[high], custom_list[i + 1]
    return i + 1


def quick_sort(custom_list, low, high):
    if low < high:
        pi = partition(custom_list, low, high)
        quick_sort(custom_list, low, pi - 1)
        quick_sort(custom_list, pi + 1, high)


clist = [4, 6, 8, 1, 11, 45, 23, 56]
quick_sort(clist, 0, 7)
print(clist)