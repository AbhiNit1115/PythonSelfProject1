def reverse():
    string = input("Please enter a value:")
    string = string[::-1]
    return string


r = reverse()
print("The reverse string is:", r)


def heap(custom_list, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and custom_list[l] < custom_list[smallest]:
        smallest = l
    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r
    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
    heap(custom_list, n, smallest)


def heap_sort(custom_list, k):
    n = len(custom_list)
    for i in range(int(n / 2) - 1, -1, -1):
        heap(custom_list, n, i)
    for i in range(n - 1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heap(custom_list, i, 0)
    custom_list.reverse()
    print(custom_list(n - k))


clist = [56, 14, 7, 98, 32, 12, 11, 50, 45, 78, 7, 5, 69]
heap_sort(clist, 5)
print(clist)