# Sometime we assign default value to the formal argument in function definition and we may not require to
# provide actual argument, In this case default argument would be used by formal argument.
# If we don't provide actual argument for formal argument explicitly while calling the function the formal
# argument will use default value else if we provide actual argument then it'll use provided value.
# Note: number of argument must be equal in formal and actual arguments no more no less.

def details(name, age):
    print(f"Name is: {name} , Age is: {age}")


# Here we have to pass some value to the actual arguments
details(name="abhishek", age=25)


# Now if we want the actual arguments to have some default values then:
def details1(name, age=25):
    print(f"Name is: {name} , Age is: {age}")


# Here even if we don't pass value of any actual argument explicitly then the default value would be called.
details1(name="abhishek")
# If we pass some other value to the default argument then precedence would be given to new value
details(name="abhishek", age=26)
