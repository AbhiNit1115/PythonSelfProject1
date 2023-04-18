def find_recursive_array(sample_array, n):
    if n == 1:
        return sample_array[0]
    else:
        return max(sample_array[n - 1], find_recursive_array(sample_array, n - 1))


list1 = [4, 1, 8, 3, 5]

rec = find_recursive_array(list1, 4)
print(rec)
print("__________________________________________")


def foo(array):
    sum1 = 0
    product = 1

    for i in array:
        sum1 += i

    for i in array:
        product *= i

    print("Sum = " + str(sum1) + ", Product = " + str(product))


list1 = [1, 3, 5, 1]
f = foo(list1)
print(f)
print("__________________________________________")


def print_pairs(array):
    for i in array:  # ----------> O(n)
        for j in array:  # ---------->O(logn)
            print(i, j)


list2 = [2, 3, 4, 5]
p = print_pairs(list2)
print(p)
print("__________________________________________")


def print_unordered_pairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(array[i], ",", array[j])


list3 = [1, 2, 3, 4]
pu = print_unordered_pairs(list3)
print("__________________________________________")


def print_unordered_pairs(array_a, array_b):
    for i in range(len(array_a)):
        for j in range(len(array_b)):
            if array_a[i] < array_b[j]:
                print(str(array_a[i]), ",", str(array_b[j]))


list4 = [2, 6, 1, 8]
list5 = [4, 1, 9, 7]
pup = print_unordered_pairs(list4, list5)
print("__________________________________________")


def print_unordered_pairs(array_a, array_b):
    for i in range(len(array_a)):
        for j in range(len(array_b)):
            for k in range(0, 2):
                print(str(array_a[i]), ",", str(array_b[j]))


list6 = [7, 2, 8, 9]
list7 = [2, 6, 5, 0]
pup = print_unordered_pairs(list6, list7)
print("__________________________________________")


def reverse_array(array):
    for i in range(0, int(len(array) / 2)):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)


list8 = [5, 9, 7, 4]
rev = reverse_array(list8)
