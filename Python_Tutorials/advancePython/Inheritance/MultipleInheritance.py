# If a child is derived from more than one parent class, then it's called multiple inheritance
# Method Resolution Order:
# In multiple inheritance scenario members of class are searched first in the current class. If they are
# not found then search continues in the parent class in depth from left to right manner without searching
# the same class twice.
# 1.) Search the child(current) class before going to its parent class.
# 2.) When a class is inherited from several classes, the search order is from left to right.
# 3.) No class is visited more than once i.e. a class in the inheritance hierarchy is traversed only once.

class Father:
    def __init__(self):
        super().__init__()
        print("I'm father class constructor")

    def show_father(self):
        print("I'm father class method")


class Mother:
    def __init__(self):
        super().__init__()
        print("I'm mother class constructor")

    def show_mother(self):
        print("I'm mother class method")


class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("I'm son class constructor")

    def show_son(self):
        print("I'm son class method")


s = Son()

# For MRO the search will start from Son. As the obj for son is created its constructor is called.
# Son has super() function inside its constructor, so it's parent from the left i.e. Father constructor is called
# Father also has super function in it so its parent "Object" class constructor is called.
# Object does not have any constructor so the search will continue down to the right side class(Mother) of
# Object class so Mother class constructor is called.
# As mother class also has super() function so it's parent class "Object" constructor is called but as
# object class is already visited the search will stop there.
