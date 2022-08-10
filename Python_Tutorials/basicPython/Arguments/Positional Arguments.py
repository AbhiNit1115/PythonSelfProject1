# Positional Arguments: These elements are passed to the functions in correct positional order. The number of
# arguments and their positions in the function definition should be equal to the number and position of the
# argument in the function call.
# Note: number of argument must be equal in formal and actual arguments no more no less.

def details(name, age):
    print("name is:", name)
    print("age is:", age)


# Here the position matters e.g. if i want output as name = abhishek and age = 25 then i have to pass first
# abhishek and then 25
details("abhishek", 25)
print("__________________________")
# In case if I reverse the order i.e. first age = 25 then name = abhishek then my output would not
# come as expected.
details(25, "abhishek")

# Positional argument will not give me any error as such in case of position reversal but one has to think
# logically before providing the actual positional arguments.
