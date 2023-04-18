def duplicate_number(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] == arr[j]:
                arr.remove(arr[i])
    print(arr)


arr = [1, 2, 3, 3, 4, 5, 5, 2]
duplicate_number(arr)


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


print(string_rotation("watter", "rettaw"))

my_string = "Hello_World"
slice = my_string[-1:-5]
print(slice)