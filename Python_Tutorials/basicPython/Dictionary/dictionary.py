# A dictionary is a group of elements in the form of key value pairs.
# Dictionary in python are unordered collection
# Dictionaries are mutable so that we can modify it's items without changing their identity.
# Key Rules:
# 1.) Keys should be unique
# 2.) Keys in dictionaries can't be repeated and must be immutable like int, string, tuple not list etc.
# 3.) Keys are case sensitive.
# Values can be of any datatype and can be duplicated.

emp = {"name": 'abhishek', "age": 23, 21.0: "yes"}


def dict1(name):
    for item in emp:
        if item['name'] == name:
            itemConfig = item



print(emp["name"])
for key in emp.keys():
    key1 = key
    print("This is a key:", key1)
for value in emp.values():
    print("This is a value:", value)

result1 = ''.join(['{0}:{1} '.format(k, v) for k, v in emp.items()])
print(result1)

# Modifying a dictionary
emp["name"] = "Abhishek Pandey"
print("After modification:", emp)

# Updating a Dictionary: If we mention a key which already exists in the dictionary then value gets updated
# instead of adding a new item. The newly added item can be placed anywhere in dictionary as it's unordered.
emp['class'] = "12 B"
print("After adding new value:", emp)
print()

# Deleting an item in dictionary
del emp['class']
# In case we want to delete the entire dictionary the use del dictionary_name

# Copy method is used to copy all the elements from existing dictionary to a new dictionary
print("Original Dictionary:", emp)
print(id(emp))
new_emp = emp.copy()
print("Copied Dictionary:", new_emp)
# If we make some changes in original dictionary then it won't impact the copied dictionary
print(id(new_emp))  # This id is different from the id of original dictionary
print()

# If we want to clear all the elements in dictionary use clear()
emp.clear()
print("After clear:", emp)
