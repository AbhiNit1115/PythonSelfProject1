

input1 = ["123", "234", "567", "767", "888", "434", "234", "543", "767", "564"]

for element in input1:
    
    if element.count(element) > 1:
        print("The anagram elements are:", element)
