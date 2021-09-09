# By default the constructor in parent class is available to the child class.
# Constructor without parameter

class Father:

    def __init__(self):
        self.money = 1000
        print("This is Parent class constructor")

    def property(self):
        print("Parent has property worth:", self.money)


class Child(Father):

    def child_property(self):
        print("This is child class having property worth: 2000")


# Now as soon we we create the object of child class automatically parent class constructor is called.
c = Child()  # when we run this object we get out as "This is Parent class constructor" (see parent class)
parent_money = c.money
print("Money inherited by child from parent is:", parent_money)
c.property()
c.child_property()
print()


# Constructor with parameter

class Father2:

    def __init__(self, m):
        self.money = m
        print("This is Parent class constructor")

    def property(self):
        print("Parent has property worth:", self.money)


class Child2(Father2):

    def child_property(self):
        print("This is child class having property worth: 2000")


# Now as soon we we create the object of child class automatically parent class constructor is called.
c2 = Child2(1000)  # when we run this object we need to pass the value for argument/parameter
parent_money = c2.money
print("Money inherited by child from parent is:", parent_money)
c2.property()
c2.child_property()
