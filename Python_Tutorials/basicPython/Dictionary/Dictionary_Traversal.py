my_dict = {"name": "abhishek", "age": 33, "occupation": "IT"}
print(my_dict.values())


def traverse_dict(my_dict):
    if 'name' in my_dict:
        name = my_dict['name']
        return name


traverse_dict(my_dict)


a = [1,2]
b = a
c = a[:]
print(a==b)
print(a==c)
print(a is b)
print(a is c)