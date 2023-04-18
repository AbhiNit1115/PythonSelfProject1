lst = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Without list comprehension
list1 = []
for i in lst:
    list1.append(i + 1)
print(list1)

# With list comprehension
list2 = [i + 1 for i in lst]
print(list2)
print()

# Range function without list comprehension
list3 = []
for i in range(5):
    list3.append(i + 1)
print(list3)
# Range function with list comprehension
list4 = [i + 1 for i in range(5)]
print(list4)
print()

# If condition without list comprehension
list5 = []
for i in range(5):
    if i % 2 == 0:
        list5.append(i)
print(list5)
# If condition with list comprehension
list6 = [i for i in range(7) if i % 2 == 0]
# The first i mentioned in list6 is the same as append function i.e. append(i), then the for loop executes
# finally the if condition is checked.
print(list6)
print()

# Nested If condition without list comprehension
list5 = []
for i in range(13):
    if i % 2 == 0 and i % 3 == 0:
        list5.append(i)
print(list5)
# If condition with list comprehension
list6 = [i for i in range(7) if i % 2 == 0 if i % 3 == 0]
# The first i mentioned in list6 is the same as append function i.e. append(i), then the for loop executes
# then first if condition executes finally the last  if condition is checked.
print(list6)
