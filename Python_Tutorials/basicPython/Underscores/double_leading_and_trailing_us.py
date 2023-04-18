# Perhaps surprisingly, name mangling is not applied if a name starts and ends with double underscores.
# Variables surrounded by a double underscore prefix and postfix are left unscathed by the Python interpeter:

class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42


print(PrefixPostfixTest().__bam__)
# output: 42

# However names that have both leading & trailing double underscores are reserved for special use in the python.
# This rule covers things like __init__ for object constructors, or __call__ to make an object callable.
# Note: It’s best to stay away from using names that start and end with double underscores (“dunders”) in your
# own programs to avoid collisions with future changes to the Python language.
