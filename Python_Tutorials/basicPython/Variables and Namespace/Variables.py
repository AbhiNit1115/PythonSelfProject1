# In Python a variable is considered as a tag that is tied to some value. Python considers values as objects
# a = 10 this will create one memory address for the value "10" and not for variable a.
# 10   --> value assigned to variable "a"
# 1456 --> memory address of value "10" and this value i.e. 10 is treated as object in python.
# the variable name i.e. "a" is just a tag to the value 10.
# now if we create a new variable b = 10, then the same memory address of 10 as created while creating variable
# a would be applicable and "b" is just another tag to that memory address.
# In short now "a" and "b" both points to same memory address i.e. 1456
# Now if do: a = 20, then a new memory address for 20 is created e.g. 1457.
# Now the question is if we call "a" then what value it would print 10 or 20?
# The answer is 20, earlier "a" was tagged to the memory location of value 10 i.e. 1456
# Now we have updated the tagged "a" to a new memory location for value 20 i.e. 1457.
# Since value 10 becomes unreferenced object, it's removed by garbage collector.
# In other programing language e.g. C, JAVA the memory address is allocated for the variable.
a = 10
print(a)  # This wil print the value with which variable a is tagged.
print(id(a))  # This will print the memory address of value 10.
a = 20
print(a)  # Now variable a is tagged with new value and this will print the new value.
print(id(a))  # Since value 10 becomes unreferenced object, it's removed by garbage collector.
