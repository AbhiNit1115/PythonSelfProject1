def first_repeated(string1):
    dict1 = []

    for i in string1:
        if i in dict1:
            print("The first repeated char is:", dict1[0])
        else:
            dict1 = i
    print(dict1)
    return ''


print(first_repeated("AApplle"))


def first(str1):
    list_repeated = []
    non_repeating = {}

    for i in range(len(str1)):
        count = 0
        for j in range(i + 1, len(str1)):
            if str1[i] == str1[j]:
                count = count + 1
                list_repeated.append(str1[i])

    print("First repeated char:", list_repeated[0])


print(first("AApple"))


def firstNonRepeatingChar(str1):
    char_order = []
    counts = {}
    for i in str1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            char_order.append(i)
    for i in char_order:
        if counts[i] == 1:
            return i
    return None


firstNonRepeatingChar("AApple")