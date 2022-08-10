# Tuple contains a group of elements that can be of same or different types and are immutable.
# i.e. they are read only so we can't modify it's elements, hence they consume less memory then list
# e.g. a =(10, 20.1,-30, 'name')
# we can not create tuple with only one element

b = (10)  # this 10 would be considered as an integer not as a tuple.
print(type(b))
b = (10,)  # this would be considered as tuple
print(type(b))
# we can also create tuple without parenthesis e.g.
a = 10, 20.1, -30, 'name'  # This would also be considered as tuple
print(type(a))

# Index: An index represents the position number of a tuple's element. It starts from [0] and -ve index
# starts from [-1]
print(a[0])
print(a[-1])
print()

# Accessing tuple without index
for element in a:
    print(element)
print()

# Accessing tuple with index
l = len(a)
for i in range(l):
    print(i, ":", a[i])
print()

# We can only delete entire tuple but not an element of tuple.
# We can't perform deletion in tuple but logically we can remove elements but actually element in the tuple
# is still not deleted, suppose we have to delete 2nd element from tuple 'x' then:
x = (1, -2, 3.4, "class")
x1 = x[0:2]
x2 = x[3:]
new_x = x1 + x2
print("New value of tuple is", new_x)
print(type(new_x))
print()

# Nested tuple using for loop
nest = (10, 20, 30, (40, 50))

l = len(nest)
for i in range(l):
    if type(nest[i]) is tuple:
        if len(nest[i]) > 1:
            n = len(nest[i])
            for j in range(n):
                print(i, ":", j, "-", nest[i][j])
    else:
        print(nest[i])
