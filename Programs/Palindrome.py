def palindrome():
    string = input("Please enter a value:")
    if string == string[::-1]:
        print("This string is palindrome")
    else:
        print("This string is not palindrome")


palindrome()
