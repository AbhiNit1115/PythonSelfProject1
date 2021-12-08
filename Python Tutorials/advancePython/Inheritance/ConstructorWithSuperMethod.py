# During constructor overriding when we want to call child as well as parent class constructor(s)
# super() method is used to call parent class "constructor" or "methods" from child class.

class Father:
    def __init__(self):
        print("This is Parent class constructor")

    def parent_property(self):
        print("Parent is having 1000")


class Child(Father):

    def __init__(self):  # child class constructor
        super().__init__()  # super() function will call the parent class constructor
        print("This is Child class constructor")  # post super function child class constructor will execute
        print()

    def child_property(self):
        print("Child has no property")


c = Child()  # when we execute this first parent class constructor would be called by super method
# then the child class constructor would be called.
c.parent_property()
c.child_property()
print()


class Father1:
    def __init__(self, p):
        self.property = p
        print("This is Parent class constructor")

    def parent_property(self):
        print("Parent is having property worth:", self.property)


class Child1(Father1):

    def __init__(self, m):  # child class constructor
        super().__init__(2000)  # pass the parameter/argument with super function
        self.money = m
        print("This is Child class constructor")  # post super function child class constructor will execute

    def child_property(self):
        print("Child has money:", self.money)


c1 = Child1(3000)  # pass the parameter/argument for child class
print()
c1.parent_property()
c1.child_property()
