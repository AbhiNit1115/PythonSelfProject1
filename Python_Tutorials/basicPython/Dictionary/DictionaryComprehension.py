dict1 = {}
# without dictionary comprehension
for i in range(10):
    # here dict[i] --> this "i" is key and i + 1 --> this "i" is value
    dict1[i] = i + 1
print(dict1)
# with dictionary comprehension
# here the first "i" is key and i + 1 --> this "i" is value
dict1 = {i: i + 1 for i in range(10)}
print(dict1)
print()

# If condition without dictionary comprehension
dict3 = {}
for i in range(10):
    if i % 2 == 0:
        dict3[i] = i + 1
print(dict3)
# If condition with dictionary comprehension
dict1 = {i: i + 1 for i in range(10) if i % 2 == 0}
print(dict1)

# Nested If condition without dictionary comprehension
dict3 = {}
for i in range(10):
    if i % 2 == 0:
        if i % 3 == 0:
            dict3[i] = i + 1
print(dict3)
# If condition with dictionary comprehension
dict1 = {i: i + 1 for i in range(10) if i % 2 == 0 if i % 3 == 0}
print(dict1)
print()

# If Else condition without dictionary comprehension
dict4 = {}
for i in range(10):
    if i % 2 == 0:
        dict4[i] = i + 1
    else:
        dict4[i] = "invalid"
print(dict4)
# If Else condition with dictionary comprehension
dict5 = {i: (i if i % 2 == 0 else "Invalid") for i in range(10)}
print(dict5)
