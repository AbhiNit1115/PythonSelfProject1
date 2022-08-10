a = {1: {"class": "Parent", "Inheritance_Applied": "Yes"},
     2: {"class": "Child", "Inheritance_Applied": "No"}}
print(a[1]['class'])

# Adding a new element to nested dictionary
a[1]['method_overloading'] = "Not Supported"
print(a[1])

# Adding a new nested dictionary to dictionary
a[3] = {"class": "Sub_Child", "Inheritance_Applied": "Maybe"}
print(a[3])

# Deleting an element from nested dictionary
del a[1]['method_overloading']
print(a[1])
