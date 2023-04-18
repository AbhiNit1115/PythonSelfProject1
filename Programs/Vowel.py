def vowel():
    string = input("Enter string: ")
    vowels = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' \
                or i == 'O' or i == 'U':
            vowels = vowels + 1
    print("Number of vowels are:", vowels)
    for char in string:
        if char in "aeiouAEIOU":
            print(char, end=', ')
    return char


vowel()
l = [10,10,1,11,9,2,11,7,2,3]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] < l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] =temp
    print(l)
