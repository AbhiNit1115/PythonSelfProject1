# A double underscore prefix causes the Python interpreter to rewrite the attribute name in order
# to avoid naming conflicts in subclasses.This is also called name mangling—the interpreter changes the name
# of the variable in a way that makes it harder to create collisions when the class is extended later.

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'


t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
print(t2.__baz)

# The self.foo variable appears unmodified as foo in the attribute list.
# self._bar behaves the same way—it shows up on the class as _bar. The leading underscore is just a convention
# in this case. A hint for the programmer.
# However with self.__baz, things look a little different. When you search for __baz in that list you’ll see
# that there is no variable with that name.
# If you look closely you’ll see there’s an attribute called _Test__baz on this object. This is name mangling
# that Python interpreter applies. It does this to protect the variable from getting overridden in subclasses
# in order to prevent accidental modification.
