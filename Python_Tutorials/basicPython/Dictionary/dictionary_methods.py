my_dict = {"name": "abhishek", "age": 33, "occupation": "IT"}

# method1: copy()
dict1 = my_dict.copy()  # this copy here is shallow copy it copies all K-V pairs from the dict
print(dict1)
print()

# method2: fromkeys() it creates new dict from given seq of elements by value provided by user
dict2 = {}.fromkeys([1, 2, 3], 0)
print(dict2)
print()

# method3: get() this method returns the value for specified key if the key is in the dict.
print(my_dict.get("name", "abhishek"))
# In case key/value doesn't exists it creates it.
print(my_dict.get("class", "10"))
print()

# method4: items() this method returns a view object that displays a list of dict K-V tuple pair
print(my_dict.items())
for k, v in my_dict.items():
    print("key is:", k, "Value is:", v)
print()

# method5: keys() displays list of all keys in the dict
print(my_dict.keys())
print()

# method6: values() displays list of all values in the dict
print(my_dict.values())
