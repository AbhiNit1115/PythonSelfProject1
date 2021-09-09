# By default the constructor in parent class is available to child class
# but what if child class also has ots own constructor
# Constructor Overriding: If we ride the constructor in both the classes then the parent class constructor
# is not available to the child class i.e. child class constructor is replacing parent class constructor

class Father:

    def __init__(self):  # parent constructor
        self.money = 1000
        print("This is Parent class constructor")

    def property(self):
        print("Parent has property worth:", self.money)


class Child(Father):

    def __init__(self):  # child constructor
        self.property = "no property"
        print("This is child class constructor")

    def child_property(self):
        print("This is child class having:", self.property)


# Now as soon we we create the object of child class then child class constructor is called.
c = Child()  # when we run this object we get out as "This is child class constructor" (see child class)
print()
c.child_property()  # we are accessing the child class method
print()


# Constructor overriding with parameter

class Father2:

    def __init__(self, m):
        self.money = m
        print("This is Parent class constructor")

    def property(self):
        print("Parent has property worth:", self.money)


class Child2(Father2):

    def __init__(self, p):
        self.property = p

    def child_property(self):
        print("This is child class is having:", self.property)


# Now the child class constructor is called
c2 = Child2("one property")  # when we run this object we need to pass the value for argument/parameter
c2.child_property()
