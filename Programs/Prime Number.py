def prime_num():
    num = int(input("Please enter a number: "))

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is a prime number")
                # break out of loop
                break
        else:
            print(f"{num} is not a prime number")


prime_num()

input1 = ["123", "234", "567", "767", "888", "434", "234", "543", "767", "564"]

for element in input1:

    if element.count(element) > 1:
        print("The anagram elements are:", element)
