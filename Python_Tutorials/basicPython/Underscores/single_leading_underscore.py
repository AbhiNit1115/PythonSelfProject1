# Single underscores are a Python naming convention indicating a name is meant for internal use.
# It is generally not enforced by the Python interpreter and meant as a hint to the programmer only.

# Take a look at the following example:

class Test:

    def __init__(self):
        self.foo = 11
        self._bar = 23


# if we instantiate this class and try to access the _bar attributes defined in its __init__ constructor then
# single underscore "_bar" will not prevent us from “reaching into” the class & accessing value of that variable.
t = Test()
print(t._bar)  # --> This will print proper output and will allow us to access the value of variable
