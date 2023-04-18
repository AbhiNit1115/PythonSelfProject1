def heapify(custom_list, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and custom_list[l] < custom_list[smallest]:
        smallest = l
    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r
    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapify(custom_list, n, smallest)


def heap_sort(custom_list, k):
    n = len(custom_list)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(custom_list, n, i)
    for j in range(-1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)
    custom_list.reverse()
    print(custom_list[len(custom_list) - k])



clist = [20, 20, 21, 1, 1, 22, 22]
heap_sort(clist, 5)
print(clist)

List1 = [{'name': 'Jhon', 'class': 12},[{'name': 'adam', 'class': 5}]]
for i in List1:
    print(i.keys())
