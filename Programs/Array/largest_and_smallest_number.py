def large_and_small(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] >= arr[j]:
                arr[i] = arr[j]
    print(arr[0], arr[-1])


def bubble_sort(custom_list):
    for i in range(len(custom_list) - 1):
        for j in range(len(custom_list) - i - 1):
            if custom_list[j] >= custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    print(custom_list)


arr = [2, -33, 12, 111, 1, 44, 55, 123, 23]
large_and_small(arr)
bubble_sort(arr)
print("___________________")


def sum_pair(arr, value):
    sum1 = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == value:
                sum1 = arr[i] + arr[j]
                pairs = str(arr[i]) + "," + str(arr[j])
    print(pairs)
    print(sum1)


arr4 = [1, 2, 3, 2, 4, 5, 2, 7]
sum_pair(arr4, 6)
