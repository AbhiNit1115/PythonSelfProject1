list1 = [29, 32, 14, 56, 97, 24, 46, 74]

temp = max(list1)

for i in range(1, len(list1)):

    num1 = list1[i]

    j = i - 1

    while j >= 0:

        num2 = list1[j]

        res = abs(num1 - num2)

        if res < temp:
            temp = res

            first_num = num1

            sec_num = num2

        j = j - 1

print(first_num, sec_num)