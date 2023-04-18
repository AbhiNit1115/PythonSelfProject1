def count_one_element_occurence(list1, x):
    count = 0
    for item in list1:
        if item == x:
            count = count + 1
    print(count)


count_one_element_occurence([1, 2, 3, 2, 3, 4, 5], 2)


def count_multiple_element_occurence(list1, element_value):
    list2 = []
    for i in list1:
        if i == element_value:
            list2.append(i)


my_string = "Test Automation"
slice4 = my_string[7:0:-1]
print(slice4)


def method1(x, y):
    print("In method1")


def method1(a, b, c):
    print("In method1 with 3 arg")


method1(1, 2, 3)
