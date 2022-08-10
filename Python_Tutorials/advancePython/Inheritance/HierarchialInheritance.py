# Hierarchical Inheritance
class Parent:

    def __init__(self):
        print("This is Father class constructor")

    def show_parent(self):
        print("This is father method")


class Son(Parent):

    def __init__(self):
        print("This is Son class constructor")

    def show_son(self):
        print("This is son method")


class Daughter(Parent):

    def __init__(self):
        print("This is daughter class constructor")

    def show_daughter(self):
        print("This is daughter method")


p = Parent()
p.show_parent()
print()
s = Son()
s.show_parent()
s.show_son()
print()
d = Daughter()
d.show_parent()
d.show_daughter()

