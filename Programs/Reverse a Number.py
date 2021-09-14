def reverse():
    num = int(input("Please enter a number:"))
    reversed_num = 0
    while num != 0:
        modulus = num % 10
        reversed_num = reversed_num * 10 + modulus
        num = num // 10
    return reversed_num


r = reverse()
print("the reversed number is:", r)

# modulus = 12345 % 10 = 5
# reversed_num = 0 * 10 + 5 = 5
# num = 12345 // 10 = 1234

# modulus = 1234 % 10 = 4
# reversed_num = 5 * 10 + 4 = 54
# num = 1234 // 10 = 123

# modulus = 123 % 10 = 3
# reversed_num = 54 * 10 + 3 = 543
# num = 123 // 10 = 12

# modulus = 12 % 10 = 2
# reversed_num = 543 * 10 + 2 = 5432
# num = 12 // 10 = 1

# modulus = 1 % 10 = 1
# reversed_num = 5432 * 10 + 1 = 54321
# num = 1 // 10 = 0
