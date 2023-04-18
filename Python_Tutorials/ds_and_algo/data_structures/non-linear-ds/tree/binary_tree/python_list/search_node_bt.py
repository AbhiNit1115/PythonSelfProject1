def partition(custom_list, high, low):

    i = low -1
    pivot = custom_list[high]

    for j in range(low, high):
        if custom_list[j] <= pivot:
            i +=1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i+1], custom_list[high] = custom_list[high], custom_list[i+1]
    return i + 1

def quick(custom_list, low, high):
    if low < high:
        pi = partition(custom_list, low, high)
        quick(custom_list, low, pi-1)
        quick(custom_list, pi+1, high)

clist = [4, 6, 8, 1, 11, 45, 23, 56]
quick(clist, 0, 7)
print(clist)
