# Variable length argument is an argument that can accept any number of values.
# The variable length argument is written with * symbol. It stores all the values in "Tuple"

def details(*detail):
    name = detail[0]  # we are using indexing and assigning it to a variable
    age = detail[1]
    phone = detail[2]
    print(f"Name is: {name}, Age is: {age}, Phone is:{phone}")


# This is in sequential order if we change the order we won't get error but output won't be logical
details("abhishek", 23, 98778678)

# Variable Length arguments gives us the liberty to pass as many arguments without giving any error.
details("jhon", 23, +43535345, "paris", "sales")


# We can even combine variable length argument with other argument types like keyword, positional, default etc.


def details1(country, *detail):
    name = detail[0]  # we are using indexing and assigning it to a variable
    age = detail[1]
    phone = detail[2]
    print(f"Country is: {country}, Name is: {name}, Age is: {age}, Phone is:{phone}")


# here india is a positional argument rest are variable length
details1("India", "Ram", 23, 456456546)
