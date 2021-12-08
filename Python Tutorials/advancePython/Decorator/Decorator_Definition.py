# A decorator is a function that accepts a function as "Parameter" and returns a function.
# Decorator takes the result of a function, modifies the result and returns it.  In decorators, functions
# are taken as the argument into another function and then called inside the wrapper function.
# Use @function_name to specify a decorator to be applied on another function
# Basically if we want to enhance a function w/o altering the function then we use decorators.

# Now if user wants to enhance the below created function w/o updating the logic inside this function the
# user needs to use decorator function(s).
def num():
    print("This function is a strict no for modification")


def decor(num):  # Decorator function with argument being passed as above created function name.
    def inner():
        print("This will execute before enhancement of the num function")
        num()
        print("This is the enhancement script")  # now whatever we're writing from this step will be considered
        # for enhancement of the num function.

    return inner  # now we're returning the inner function


# Now there are 2 ways to call this decorator function, the first way:
updated_result = decor(num)
print(updated_result())
print()


# The other way is simple just use @decorator method name above the function for which enhancement is needed.
def decor1(num1):  # Decorator function with argument being passed as above created function name.
    def inner():
        print("This will execute before enhancement of the num function")
        num()  # we are calling the num function
        print("This is the enhancement script")  # now whatever we're writing from this step will be considered
        # for enhancement of the num function.

    return inner  # now we're returning the inner function


@decor1  # This will reduce the redundant steps used in the first way
def num1():
    print("This function is a strict no for modification")


# In order to call the function just call the original function name.
num1()


