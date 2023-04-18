def max_sum1(arr, k):
    max_sum = 0
    window_sample = 0
    start = 0

    for i in range(len(arr)):
        window_sample += arr[i]
        if (i - start + 1) == k:
            max_sum = max(max_sum, window_sample)
            window_sample -= arr[start]
            start += 1
    print(max_sum)


arr = [10, 2, 3, 4, 5, 6]
max_sum1(arr, 4)


def sum_of_array(list1, k):
    total_ele = len(list1)
    # i = 0
    # k = 2
    for i in range(0, total_ele-1):
        temp = list1[i]
        for index in range(i + 1, i + k):
            temp += list1[index]
        print(temp)


list1 = [10, 2, 3, 4, 5, 6]
sum_of_array(list1, 3)

list1 = [29, 32, 14, 56, 97, 24, 46, 74]
# Write a program to find 2 closest elements in the given list.

l1 = []  # for storing differnce
l2 = []  # for storing closest numbers

if list1[0] > list1[1]:
    difference = list1[0] - list1[1]
else:
    difference = list1[1] - list1[2]

l1.append(difference)

for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[j] > list1[i + 1]:
            difference = list1[0] - list1[i + 1]
        else:
            difference = list1[i + 1] - list1[0]

        if difference < l1[0]:
            l1.append(difference)
            l1.pop(0)
            l2.append(list1[0])






