a = [1, 2]
b = a
c = a[:]
print(a == b)
print(a == c)
print(a is b)
print(a is c)

list = ["apple", "banana", "pineapple"]

list2 = list[::]
print(list2)

mylist1 = [x * x for x in range(3)]
mylist2 = (x * x for x in range(3))
print(mylist1)
print(id(mylist2))
