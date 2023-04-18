
str1 = "aaa"  # str1: Fired
str2 = "aaa"  # str2: Fried
count = 0  # count: 0

for i in str1:  # i: F

    for j in str2:  # j: F

        if i == j:  # here the condition is true
            count = count + 1
        # Now as the counter reaches one the inner loop will execute again and it will compare all the char of
        # str2 with first char of str1

if count == len(str1):

    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")

str1 = "fired"
str2 = "rfied"
