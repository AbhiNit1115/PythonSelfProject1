string = "aapple"

print("Duplicate characters in a given string: ")
for i in range(0, len(string)):
    count = 1
    for j in range(i + 1, len(string)):
        if string[i] == string[j] and string[i] != ' ':
            count = count + 1

    if count > 1 and string[i] != '0':
        print(string[i], " - ", count)

list1 = [2, 1, 3, 2, 2, 3, 4, 5, 2, 3, 1]

out = []
for number in list1:
    if number not in out:
        out.append(number)  # --[2,1,3,4,5]

print(out)

