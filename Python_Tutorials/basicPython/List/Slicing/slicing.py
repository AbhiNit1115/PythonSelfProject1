# Slicing on list can be used to retrieve a piece of list that contains group of elements.
# Syntax: new_list_name = list_name[start:stop:stepsize]
# If we don't give start value then by default it's '0' and if we don't give step size by default its '1'

x = [101, 102, 103, 104, 105, 106, 107]
print("Original list is:")
length = len(x)
for i in range(length):
    print(i, '=', x[i])
print(x[::])

print()
print("from 1st position to 4th position:")
a = x[1:5]
for i in a:
    print(i)

print()
print("from 0th position to last position:")
a = x[0:]
for i in a:
    print(i)

print()
print("Without start value and only end value from 0th to 4th position:")
a = x[:5]
for i in a:
    print(i)

print()
print("Last 4 elements")
a = x[-4:]
for i in a:
    print(i)

print()
print("from 0th position to 6th position step size 2:")
a = x[0:7:2]
for i in a:
    print(i)

print()
print("from -5th position to -2th position step size 2:")
a = x[-5:-2]
for i in a:
    print(i)

y = ['india', 'country']
print("This will print:", y[-1][-1])

list1 = "abcd"
reverse = list1[1:3:-1]
print(reverse)
