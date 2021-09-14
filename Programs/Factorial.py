def factorial():
    fact = 1
    num = int(input("Please enter a number:"))

    if num < 0:
        print("Please enter a positive number")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            fact = fact * i
            print("The factorial of", num, "is", fact)


factorial()
