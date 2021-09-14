# Now what if we want to add multiple function(s) in order to enhance our original method/function
# E.g. there is a num function which returns 10, now we want to add and multiply 5 to the return of
# num function, so we create 2 decorator function to enhance the original num function.


# Decorator function number one for addition
def decor(num):
    def inner():
        a = num()
        add = a + "three"
        return add

    return inner()


# The original num function
@decor
def num():
    x = "One"
    y = "Two"
    z = x + y
    return z


# Now how to call both the decorators
print(num())
