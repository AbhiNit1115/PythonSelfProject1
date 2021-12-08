# Keyword Arguments: These arguments are passed to a function with name-value pair so keyword argument can
# identify the formal arguments by their names. The keyword arguments name formal arguments name must match
# here we don't need to worry about the position of the arguments.
# Note: number of argument must be equal in formal and actual arguments no more no less.

def details(name, age):
    print(f"Name is:{name} , Age is: {age}")


# Here the position does not matters e.g. if we want output as name = abhishek and age = 25 then
# we can pass arguments in any order
details(name="abhishek", age=25)
# If we don't assign name-value pair to name and age argument & directly pass them it becomes positional argument
details("abhishek", 25)  # Positional argument
