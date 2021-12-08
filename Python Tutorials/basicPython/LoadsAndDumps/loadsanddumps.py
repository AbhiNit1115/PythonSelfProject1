# JSON data are string format so directly we can't extract any information
# json.loads() --> This function loads JSON data and convert it to a dictionary.
# json.dumps() --> This function converts a python dictionary to JSON format string.
# In order to use JSON import JSON module, JSON is not inbuilt in python.

import json

a = {"name": "abhishek", "company": "google"}
print(type(a))  # here a is a dictionary the class will show as dictionary
print(a)

b = json.dumps(a)  # here variable "a" was dictionary, dumps has converted this dictionary to JSON string format.
print(type(b))  # the class will show as str(JSON String)
print(b)

# Now in order to use this JSON string in python we will use loads function to convert string to dictionary.
c = json.loads(b)
print(type(c))
print(c)

d = {"name": "vivek", "company": "apple"}
e = json.dumps(d)  # here variable "d" was dictionary, dumps has converted this dictionary to JSON string format.
print(type(e))  # the class will show as str(JSON String)
print(e[0:6])  # here we are printing the 0th index of string till 6th index
