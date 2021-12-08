# Now what if we want to add multiple function(s) in order to enhance our original method/function
# E.g. there is a num function which returns 10, now we want to add and multiply 5 to the return of
# num function, so we create 2 decorator function to enhance the original num function.


# Creating a decor function for multiplication
def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi

    return inner


def decor(num):  # Creating a decor function for addition
    def inner():
        a = num()
        add = a + 5
        return add

    return inner


def num():  # Modifying this function is strict no.
    return 10


num = decor(decor1(num))
print(num())

# The mechanism of calling decorator: When this code executes it goes to line 7 i.e. decor1 function and it
# sees that decor is not called, so it goes to line 16 i.e. decor func sees that it's also not getting called
# then it goes to line 25 num function that is also not getting called next it goes to line 29 i.e. object
# creation for num function along with decorators, so the inside function will execute first i.e.
# decor1(num) which will give the result as 50, then it will execute the outside decor function which will
# add 5 more to the multiplied result i.e. 50 + 5 = 55
