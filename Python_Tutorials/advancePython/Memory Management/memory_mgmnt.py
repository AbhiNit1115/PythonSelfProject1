# Types of memory allocation:
# 1.) Static Memory allocation: When we know the exact size and type of memory before execution.
# 2.) Dynamic Memory allocation: This type of memory allocation happens at runtime.

# Python uses dynamic memory allocation as in Python everything is an object. Every obj has an obj_ value,
# obj_reference_count and obj_type.
# Reference: A reference is a name/container obj that points to another obj. Obj_Reference count is like number
# of references to that object. So if we say
x = 10
print(id(x))  # the id function prints the memory address for the reference variable 'x'
# here x hold the memory address for the value 10. Now lets create another variable
y = 10
print(id(y))
# here the object value i.e. '10' is same but the reference variable i.e. 'y' is different. So in Python if the
# object value is same for different reference variable(s) then python just increases the reference count for
# that object. From our example x = 10 here the reference count for reference variable x is +1 now when we
# create another reference count for the same object value i.e. 10 as we did y=10 here the reference count
# get increased by +1 and total reference variable count becomes 2. Hence the diffrent reference variable
# points to the same memory address.

# Like we can increase the reference variable we can also decrease it as well. So when the reference variable
# goes to '0' then garbage collector gets activated.
# Garbage Collection: A way for program to automatically release memory when the object taking up that space
# is no longer in use.

# Heap Memory: Object value i.e. '10' is stored in the heap memory.
# Stack Memory: Reference variable(x and y)memory address i.e. 3435435 is stored in stack memory.
